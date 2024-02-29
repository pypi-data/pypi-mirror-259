import redis
from contextlib import contextmanager


class ServiceRedis:
    def __init__(self, connect_info: dict):
        """redis服务初始化

        提供redis pool对象

        Args:
            connect_info: dict包括host, port, db, password

        """

        connect_info = connect_info.copy()
        remove_k = [v for v in connect_info if v not in ('host', 'port', 'db', 'password')]
        for k in remove_k:
            del connect_info[k]
        self.pool = redis.ConnectionPool(**connect_info)

    @contextmanager
    def with_conn(self):
        """上下文管理，提供redis conn

        Usage:
            >>> with obj.with_conn() as conn:
            >>>     # do sth with conn

        """

        try:
            conn = redis.Redis(connection_pool=self.pool, decode_responses=True)
            yield conn
        except:
            raise
        finally:
            conn.close()