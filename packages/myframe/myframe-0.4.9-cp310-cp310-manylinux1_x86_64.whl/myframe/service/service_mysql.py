import logging
import pymysql
import pandas as pd
from loguru import logger as loggeruru
from tenacity import Retrying, stop_after_attempt, RetryError, retry
from sqlalchemy import create_engine, MetaData, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from dbutils.pooled_db import PooledDB
from contextlib import contextmanager
from urllib.parse import quote_plus as urlquote


class ServiceMysql:
    def __init__(self, connect_info: dict, logger: logging.Logger):
        """初始和mysql服务

        提供engine，pool，base等mysql相关的功能

        Args:
            connect_dict: 连接信息包括user, password, host, port, db; sqlalchemy_conn_num可选，sqlalchemy连接数，默认4;
                          pool_conn_num可选，mysql pool的连接数，默认4。

        """

        loggeruru.info("create mysql server", str(connect_info))
        if "sqlalchemy_conn_num" in connect_info:
            self._sqlalchemy_conn_num = connect_info['sqlalchemy_conn_num']
        else:
            self._sqlalchemy_conn_num = 4

        if "pool_conn_num" in connect_info:
            self._pool_conn_num = connect_info['pool_conn_num']
        else:
            self._pool_conn_num = 4

        self._connect_info = connect_info
        self._logger = logger
        connect_str = "mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8".format(
            user=connect_info['user'],
            password=urlquote(connect_info['password']),
            host=connect_info['host'],
            port=connect_info['port'],
            db=connect_info['db']
        )
        self.engine = create_engine(
            connect_str,
            pool_size=self._sqlalchemy_conn_num,
            max_overflow=10,  # 当超出最大poolsize时候，可以允许在开启n个新连接，后期可以被关闭
            pool_pre_ping=True,
            pool_recycle=3600)
        # self.metadata = MetaData()
        # self.metadata.reflect(bind=self.engine)
        self.base = automap_base()
        # self.base.prepare(self.engine, reflect=True)
        self.base.prepare(autoload_with=self.engine)  # 2.0
        self.get_session = sessionmaker(bind=self.engine)

        if self._pool_conn_num > 0:
            self.pool = self._get_mysql_pool(
                host=connect_info['host'],
                port=connect_info['port'],
                user=connect_info['user'],
                password=connect_info['password'],
                db=connect_info['db']
            )

    def _get_mysql_pool(self, host, port, user, password, db):
        # print("create db pool with %s@%s:%s" % (user, host, port))
        pool = PooledDB(
            creator=pymysql,
            maxconnections=self._pool_conn_num,
            mincached=1,
            maxcached=self._pool_conn_num,
            maxshared=3,
            blocking=True,
            maxusage=None,
            setsession=[],
            ping=1,
            host=host,
            port=int(port),
            user=user,
            password=password,
            db=db,
            charset='utf8',
            #use_unicode=True
        )
        return pool

    @contextmanager
    def with_session(self):
        """上下文管理，sqlalchemy session

        Usage:
            >>> with service_mysql.with_session() as session:
            >>>     # do sth with session
            >>>     print()

        """

        try:
            session = self.get_session()
            session.begin()
            yield session
            session.commit()
        except Exception as e:
            self._logger.warning("error happen in session msg=%s" % str(e))
            raise Exception(str(e))
        finally:
            session.close()

    @contextmanager
    def with_conn(self):
        """上下文管理pool conn

        Usage:
            >>> with service_mysql.with_conn() as conn:
            >>>     # do sth with conn

        """

        try:
            conn = self.pool.connection()
            yield conn
            conn.commit()
        except Exception as e:
            self._logger.warning("error happen in conn msg=%s" % str(e))
            raise Exception(str(e))
        finally:
            conn.close()

    @retry(stop=stop_after_attempt(3))
    def read_sql_with_session(self, sql:str) -> pd.DataFrame:
        """使用pd.read_sql_query查询sql

        使用tenacity默认尝试3次，读取sql，返回pd.DataFrame

        """

        with self.with_session() as session:
            return pd.read_sql_query(sql, session.get_bind())

    def safe_execute_sql_with_conn(
            self,
            sql_template: str,
            param: dict,
            is_read: bool = True):
        # sql_template:  select * from xxx where name = %(name)s
        # param: dict(name='xxx')

        with self.with_conn() as conn:
            cur = conn.cursor()
            rst = cur.execute(sql_template, param)
            if not is_read:
                return rst
            else:
                df = pd.DataFrame(cur.fetchall(), columns=[v[0] for v in cur.description])
                return df

    # @retry(stop=stop_after_attempt(2))
    # def safe_execute_sql_with_session(self, sql_text: sqlalchemy.TextClause, param:dict):
    #    with self.with_session() as session:
    #        rst = session.execute(sql_text, param)
    #        return rst

    @retry(stop=stop_after_attempt(2))
    def safe_read_sql(self, sql_template: str, param: dict, conn) -> pd.DataFrame:
        """使用pool的conn，用参数模板读取sql，避免依赖注入

        Args:
            sql_template: 支持参数模板的sql字符串，example: select * from xxx where name = %(name)s
            param: dict对象，example: dict(name='xxx')
            conn: pool conn

        Returns:
            DataFrame

        """
        # sql_template:
        # param: dict(name='xxx')
        cur = conn.cursor()
        cur.execute(sql_template, param)
        rst = pd.DataFrame(cur.fetchall(), columns=[v[0] for v in cur.description])
        cur.close()
        return rst
