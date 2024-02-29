import json
from logging import Logger

import requests
import contextvars
from typing import List, Tuple, Any
from tenacity import Retrying, stop_after_attempt, RetryError, retry
from myframe.util import Tool


class ServiceHpptClient:
    def __init__(self, connect_info: dict, contextvar_g: contextvars.ContextVar, logger: Logger):
        """httpclient服务

        Args:
            connect_info: dict包括address
            contentvar_g: session相关的变量
            logger: 日志对象

        """

        self._connect_info = connect_info
        self._contextvar_g = contextvar_g
        self._logger = logger
        self.url = f"http://{connect_info['address']}"

    def call(self, name: str, data: dict = None, metadata: List[Tuple] = None, timeout: int = 10) -> Any:
        """http请求

        http的get和post请求。metadata中添加syz_accesstoken，用于jwt认证；请求返回信息格式(code, msg, data)

        Args:
            name: url地址
            data: post数据，当非None使用post方法请求，当None使用get方法请求
            metadata: header设置
            timeout: 请求超时时间

        Return:
            返回请求的data内容

        """

        headers = {}

        _data = self._contextvar_g.get()
        if "syz_accesstoken" in _data:
            headers['Authorization'] = "Bearer " + _data['syz_accesstoken']
        if "syz_traceid" in _data:
            headers['syz-traceid'] = _data['syz_traceid']  # http header 使用中划线
        if metadata:
            for item in metadata:
                headers[item[0]] = item[1]

        # TODO 在app项目中转发header等信息
        try:
            for attempt in Retrying(stop=stop_after_attempt(2)):
                with attempt:
                    _path = Tool.url_join([self.url, name])
                    self._logger.debug(f"http call {_path}")
                    if data is None or len(data) == 0:
                        req = requests.get(_path, headers=headers, timeout=timeout)
                    else:
                        req = requests.post(_path, json=data, headers=headers, timeout=timeout)
                    rst = json.loads(req.text)
                    if 'code' in rst and rst['code'] in (0, '0'):
                        return rst['data']
                    else:
                        print(f"error happen in http call with rst={rst}")
                        raise Exception(rst['msg'])
        except RetryError as e:
            e.reraise()


