import jwt
import time
import datetime
from myframe.util import ExceptionAuthFailed


class ServiceJwt:
    def __init__(self, info: dict):
        """初始jwt服务

        Args:
            info: dict包括secret_key和timeout（可选，默认3600）

        """

        if 'secret_key' not in info:
            raise Exception("jwt_secret_key not in info, please check")
        self._secret_key = info['secret_key']
        self._timeout = int(info.get("timeout", 3600))

    def create_access_token(self, user_name: str, timeout: int = None) -> str:
        """创建token

        token payload中包括user_name和exp，exp为创建时的time+timeout

        Args:
            user_name: 用户名
            timeout: token时长，不指定使用self._timeout

        Return:
            token str
        """

        _timeout = timeout if timeout else self._timeout
        payload = {
            "user_name": user_name,
            "exp": time.time() + _timeout
        }
        token = jwt.encode(payload, self._secret_key, algorithm="HS256")
        return token

    def verify_access_token(self, token: str) -> str:
        """验证token

        检验token，判断是否超时，返回user_name

        Args:
            token: token字符串

        Raises:
            ExceptionAuthFailed: 验证失败Exception

        """
        try:
            data = jwt.decode(token, self._secret_key, algorithms=["HS256"])
            expire = data.get("exp")
            # print(datetime.datetime.utcnow(), datetime.datetime.utcfromtimestamp(expire))
            if expire is None:
                raise ExceptionAuthFailed()
            if datetime.datetime.utcnow() > datetime.datetime.utcfromtimestamp(expire):
                raise ExceptionAuthFailed()
            return data['user_name']
        except jwt.PyJWTError:
            raise ExceptionAuthFailed()