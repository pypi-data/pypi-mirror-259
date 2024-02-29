import os
import sys
import platform
import json
from pydantic import BaseModel, validator
from typing import List, Optional
from loguru import logger
from myframe import util    # 触发认证代码


_PROJECT_TYPE = ["project_package"]
_CONFIG_TYPE = ["package", "fastapi", "flask"]
_SERVICE_TYPE = ['mysql', 'redis', 'http_client', 'jwt', 'casbin', 'cdn']


class FrameModelService(BaseModel):
    # 服务配置
    name: str
    type: str
    info: dict

    @validator('type')
    def check_type(cls, value):
        if value not in _SERVICE_TYPE:
            raise Exception(f"service type must in {_SERVICE_TYPE}, not {value}")
        return value


class FrameModelConfig(BaseModel):
    # 项目配置
    project_name: str
    # project_path: str
    env: str
    version: str
    type: str

    # log 相关
    log_level: Optional[str] = "DEBUG"
    log_column_contextvar: Optional[str] = "myapp,myip,username,path,traceid"
    log_column_msg: Optional[str] = ""

    # api 相关
    api_port: Optional[int] = None
    api_prefix: Optional[str] = None
    api_workers: Optional[int] = 4
    api_auto_section: Optional[str] = 'ALL'

    other: Optional[dict] = None
    services: Optional[List[FrameModelService]] = None

    @validator('type')
    def check_type(cls, value):
        if value not in _CONFIG_TYPE:
            raise Exception(f"config type must in {_CONFIG_TYPE}, not {value}")
        return value


class FrameModelProject(BaseModel):
    # 配置文件解析配置
    mode: str  # 项目模式
    version: str  # 解析模式
    config_filename: str  # 配置文件地址
    config: FrameModelConfig  # 具体的配置

    @validator("mode")
    def check_mode(cls, value):
        if value not in _PROJECT_TYPE:
            raise Exception(f"project mode must in {_PROJECT_TYPE}, not {value}")
        return value

    @validator("config_filename")
    def check_config_filename(cls, value):
        value = os.path.normpath(value)
        if not os.path.exists(value):
            return Exception(f"config_filename={value} not exist")
        return value


def _load_config(filename: str) -> dict:
    project_name = os.path.basename(filename).replace("-config.json", "")
    project_prefix = f'{project_name.upper()}'

    def _create_dir(p):
        if not os.path.exists(p):
            try:
                os.makedirs(p)
            except Exception as e:
                print(str(e))
                raise Exception()
        return p

    dir_user = os.path.expanduser("~")
    config = None
    filename = os.path.abspath(filename)

    # for p in ["/etc", filename]:
    #    if p == "/etc":
    #        if platform.platform().startswith("Windows"):
    #            continue
    #        else:
    #            f = os.path.join(p, os.path.basename(filename))
    #    else:
    #        f = p

    if os.path.exists(filename):
        logger.debug(f"use config filename {filename}")
        with open(filename, "r", encoding='utf-8') as _f:
            config = json.load(_f)

        # 从环境变量中再取信息，方便docker-compose配置
        # 目前只处理当前配置文件中存在的str和int配置
        for k in config:
            _old_v = config[k]
            if isinstance(_old_v, str) or isinstance(_old_v, int):
                _v = os.getenv(k, None)
                if _v:
                    if isinstance(config[k], int):
                        config[k] = int(_v.strip())
                    else:
                        config[k] = _v.strip()
            # break

    if config:
        port = config.get(f'{project_prefix}__API__PORT', None)
        if port:
            path_pat = f"{project_name}-{port}"
        else:
            path_pat = project_name
        # find other
        if f'{project_prefix}__OTHER' not in config:
            config[f'{project_prefix}__OTHER'] = dict()
        other = config[f'{project_prefix}__OTHER']
        if os.getenv('__RUN__IN__DOCKER') == 'YES':
            other['path_log'] = _create_dir(f"/myapp-log/{path_pat}")
            other['path_data'] = _create_dir(f"/myapp-data/{path_pat}")
            other['path_upload'] = _create_dir("/myapp-upload")
        else:
            other['path_log'] = _create_dir(os.path.join(dir_user, f".myapp-log/{path_pat}"))
            other['path_data'] = _create_dir(os.path.join(dir_user, f".myapp-data/{path_pat}"))
            other['path_upload'] = _create_dir(os.path.join(dir_user, ".myapp-upload/"))
        config['other'] = other

        # 简单校验：配置文件名是否和具体内容的project_name一致
        if config.get(f"{project_prefix}__PROJECT__NAME", None) == project_name:
            pass
            # logger.debug("check success: project_name")
        else:
            raise Exception()

        # 简化处理
        _config = dict()
        for k, v in config.items():
            _config[k.replace(f"{project_prefix}__", "").replace("__", "_").lower()] = v
        # _config['project_path'] = project_path    # TODO 是否可以移除
        return _config
    else:
        raise Exception("cannot find config file")


def _load_from_given_file(config_filename: str):
    if not os.path.exists(config_filename):
        raise Exception(f"{config_filename} not exists")

    logger.debug(f"load config: {config_filename}")
    data = _load_config(config_filename)
    config = FrameModelConfig(**data)
    project_config = FrameModelProject(
        mode='project_package',
        version='v0.1.0',
        config_filename=config_filename,
        config=config
    )
    return project_config


def frame_init_project_config(config_filename: str = None):
    if config_filename:
        return _load_from_given_file(config_filename)

    # 寻找当前项目信息，确保project_name-config.json文件存在
    logger.debug("try find config file")

    def _is_project_dir(_path):
        # 判断是不是项目文件夹
        if os.path.exists(os.path.join(_path, f"{os.path.basename(_path)}-config.json")) and \
                os.path.dirname(_path) in sys.path:
            return True
        return False

    _guess_version = "v0.1.0"
    path = os.path.abspath(os.getcwd())
    deep = 0
    while True:
        if _is_project_dir(path):
            project_name = os.path.basename(path)
            project_config_filename = os.path.join(path, f"{project_name}-config.json")
            break
        path = os.path.dirname(path)
        deep += 1
        if deep > 10:
            logger.debug("project system can not location project path")
            raise Exception("project can not location project path")

    if not platform.platform().startswith("Windows"):
        _filename = f"/etc/{os.path.basename(project_config_filename)}"
        if os.path.exists(_filename):
            return _load_from_given_file(_filename)

    return _load_from_given_file(project_config_filename)
