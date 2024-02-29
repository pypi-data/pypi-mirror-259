import os
import sys
import json
import copy
import datetime
import contextvars
import logging
from loguru import logger as loguru_logger
from concurrent_log_handler import ConcurrentRotatingFileHandler


def service_init_logger(
        project_name: str = None,
        path_log: str = None,
        level=logging.DEBUG,
        contextvar_g: contextvars.ContextVar = None,
        log_column_contextvar: str = None,
        log_column_msg: str = None
) -> logging.Logger:
    """json format的logger初始化

    Args:
        project_name: 项目名称
        path_log: 文件log位置，使用ConcurrentRotatingFileHandler支持多线程
        level: 日志输出level
        contextvar_g: context var用于保存http请求session信息
        log_column_contextvar: 从context var中提取信息，保存到输出的日志json中，默认为myapp、myip、username、path、traceid
        log_column_msg: 从传入的dict日志信息中提取特殊的列放置到全局的json中

    Returns:
        返回logging.Logger对象

    """

    loguru_logger.info(f"create my logger {project_name} at {path_log}")
    if log_column_contextvar is None:
        _log_column_contextvar = ['myapp', 'myip', 'username', 'path', 'traceid']
    else:
        _log_column_contextvar = [v.strip() for v in log_column_contextvar.split(",")]
    if log_column_msg is None:
        _log_column_msg = []
    else:
        _log_column_msg = [v.strip() for v in log_column_msg.split(",")]
    loguru_logger.info(f"log column contextvar: {str(_log_column_contextvar)}")
    loguru_logger.info(f"log_column msg       : {str(_log_column_msg)}")

    class _JSONFormatter(logging.Formatter):
        remove_attr = ['levelno', 'threadName', 'processName',
                       'exc_text', 'stack_info', 'created', 'msecs',
                       "relativeCreated", "args", 'pathname', "exc_info"]
        retain_attr = ['name', 'levelname', 'time', 'process', 'thread', 'module', 'filename', 'lineno', 'funcName',
                       'msg']

        def set_contextvar_g(self, g):
            self.contextvar_g = g

        def format(self, record):
            extra = self.build_record(record)
            self.set_format_time(extra)

            # 从全局变量contextvar_g中提取部分信息到全局json中
            def _add_info(_name):
                extra[_name] = ''
                _data = contextvar_g.get()
                if _data:
                    _k = 'syz_' + _name
                    if _k in _data and _data[_k]:
                        extra[_name] = _data[_k]

            # add contextvar column，myapp myip username path traceid
            if contextvar_g is not None and len(_log_column_contextvar) > 0:
                for v in _log_column_contextvar:
                    _add_info(v)

            if record.exc_info:
                extra['exc_info'] = self.formatException(record.exc_info)

            msg = copy.deepcopy(record.msg)
            if isinstance(msg, dict):
                # 从msg中提取部分信息到全局json中
                for k in msg:
                    if k in _log_column_msg:
                        extra[k] = msg[k]
                for k in _log_column_msg:
                    if k in msg:
                        del msg[k]
                extra['msg'] = msg
            else:
                extra['msg'] = msg
            return json.dumps(extra, ensure_ascii=False)

        @classmethod
        def build_record(cls, record):
            return {
                attr_name: str(record.__dict__[attr_name])
                for attr_name in record.__dict__ if attr_name not in _JSONFormatter.remove_attr
            }

        @classmethod
        def set_format_time(cls, extra):
            now = datetime.datetime.now()
            format_time = now.strftime("%Y-%m-%dT%H:%M:%S" + ".%06d" % now.microsecond)
            extra['time'] = format_time
            return format_time

    logger = logging.getLogger(__name__ if project_name is None else project_name)

    json_format = _JSONFormatter()
    # if contextvar_g is not None:
    #    json_format.set_contextvar_g(contextvar_g)

    # file
    if path_log:
        # 多进程会有问题
        # filehandler = TimedRotatingFileHandler(
        #    os.path.join(path_log, f"{project_name}.log"),
        #    when="D",
        #    interval=1,
        #    backupCount=30
        # )
        # filehandler = WatchedFileHandler(os.path.join(path_log, f"{project_name}-{time.time()}.log"))
        __filename = os.path.join(path_log, f"{project_name}.log")
        loguru_logger.info(f"log filename {__filename}")
        filehandler = ConcurrentRotatingFileHandler(
            os.path.join(path_log, f"{project_name}.log"),
            "a",
            1024 * 1024 * 100,
            20
        )
        filehandler.setFormatter(json_format)
        logger.addHandler(filehandler)

    #if use_stream_log:
    # console
    stream_handler = logging.StreamHandler(stream=sys.stdout)
    # stream_handler.setFormatter(logging.Formatter('%(asctime)s,%(name)-12s,%(levelname)-8s,%(message)s'))
    stream_handler.setFormatter(json_format)
    logger.addHandler(stream_handler)

    logger.setLevel(level)

    yield logger
