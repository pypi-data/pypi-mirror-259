import copy
import time
import datetime
import inspect
import hashlib
from myframe.util import ExceptionAuthFailed


class ServiceParamsign:
    def __init__(self, info: dict, user_token_func=None):
        if "secret_key" not in info:
            raise Exception("secret_key not in info, please check")
        self._secret_key = info['secret_key']
        self._timeout = int(info.get("timeout", 60))
        if user_token_func:
            if inspect.isfunction(user_token_func):
                self._user_token_func = user_token_func
            else:
                raise Exception("user_token_func is not func")
        else:
            self._user_token_func = lambda x: self._secret_key

    def _cal_sign(self, param: dict):
        param = copy.deepcopy(param)
        # 如果参数里面有user_name，通过user_name寻找到对应的secret_key，用于拓展未来的程序权限控制
        if "user_name" in param:
            user_name = param['user_name']
            token = self._user_token_func(user_name)
        else:
            token = self._secret_key
        s = ""
        for k in sorted(param.keys()):
            s += "%s=%s" % (k, str(param[k]))
        s = token + s + token
        return hashlib.md5(s.encode("utf-8")).hexdigest()

    def generate_sign(self, param: dict, timeout: int = None) -> dict:
        if '__exp' in param or '__sign' in param:
            raise Exception()
        param = copy.deepcopy(param)
        _timeout = timeout if timeout else self._timeout
        param['__exp'] = time.time() + _timeout
        sign = self._cal_sign(param)
        param['__sign'] = sign
        return param

    def confirm_sign(self, param: dict) -> bool:
        param = copy.deepcopy(param)
        if '__exp' not in param or '__sign' not in param:
            return ExceptionAuthFailed()
        expire = param.get("__exp")
        try:
            if datetime.datetime.utcnow() > datetime.datetime.utcfromtimestamp(expire):
                raise ExceptionAuthFailed()
        except:
            raise ExceptionAuthFailed()
        __sign = param['__sign']
        del param['__sign']
        if __sign != self._cal_sign(param):
            raise ExceptionAuthFailed()
        else:
            del param['__exp']
            return param

