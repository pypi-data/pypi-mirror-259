import os
import uuid
from logging import Logger

import oss2
from threading import Lock
from myframe import Tool


class ServiceCdn:
    def __init__(self, info: dict, logger: Logger=None):
        """cdn服务

        Args:
            info: dict包括access_key_id, access_key_secret, endpoint, need_auth(true/false), url_prefix

        """

        self._lock = Lock()
        self._access_key_id = info['access_key_id']
        self._access_key_secret = info['access_key_secret']
        self._bucket_name = info['bucket_name']
        self._endpoint = info['endpoint']
        self._need_auth = info['need_auth']
        self._url_prefix = info.get('url_prefix', None)
        if self._url_prefix:
            if not self._url_prefix.endswith("/"):
                self._url_prefix += "/"

        self.auth = oss2.Auth(self._access_key_id, self._access_key_secret)
        self.bucket = oss2.Bucket(self.auth, self._endpoint, self._bucket_name)
        self.logger = logger

    def upload(self, filename: str, name: str = None, path: str = None) -> str:
        """上传

        Args:
            filename: 文件名
            name: 上传cdn文件名
            path: 上传cdn路径名

        Return:
            返回cdn的文件名

        """

        headers = {}
        if not name:
            if filename.endswith("png"):
                name = os.path.split(filename)[-1]
                if not Tool.is_uuid(name.split(".")[0]):
                    name = str(uuid.uuid1())
                headers = {
                    'Content-Type': 'image/png',
                    'Content-Disposition': 'inline'
                }
            else:
                name = str(uuid.uuid1())
        if path:
            name = f"{path}/{name}"
        try:
            self.bucket.put_object_from_file(
                name,
                filename,
                headers=headers
            )
            return name
        except:
            # 如果报错，重新初始化下
            with self._lock:
                self.auth = oss2.Auth(self._access_key_id, self._access_key_secret)
                self.bucket = oss2.Bucket(self.auth, self._endpoint, self._bucket_name)
            self.bucket.put_object_from_file(
                name,
                filename,
                headers=headers
            )
            return name

    def get_oss_url(self, name: str, timeout: int = 3600) -> str:
        """返回oss url地址

        Args:
            name: 文件名
            timeout: 如果need_auth，返回带过期时间的oss url地址

        Return:
            oss url地址

        """

        exist = self.bucket.object_exists(name)
        if exist:
            if not self._need_auth:
                url = self._url_prefix + name
                return url
            else:
                url = self.bucket.sign_url('GET', name, timeout, headers=dict(), slash_safe=True)
                url = url.replace(
                    "gtjaqh-research-chart.oss-cn-shanghai.aliyuncs.com",
                    "research-chart-cdn.gtjaqh.com")
                return url
        else:
            return None
