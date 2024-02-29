import os
import re
import time
import redis
import casbin
import threading
import casbin_sqlalchemy_adapter
from logging import Logger
from sqlalchemy import create_engine, MetaData, Column, Integer, String
from urllib.parse import quote_plus as urlquote

from myframe.service.service_redis import ServiceRedis


class ServiceCasbin:
    def __init__(self, info: dict, logger: Logger):
        """casbin服务

        权限管理服务，使用redis channel更新配置，需要obj.set_auto_reload(redis_service_obj)

        Args:
            info: dict包括user, password, host, port db, tb
            logger: 日志对象

        """

        connect_str = "mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8".format(
            user=info['user'],
            password=urlquote(info['password']),
            host=info['host'],
            port=info['port'],
            db=info['db']
        )

        self._group_pat = re.compile("^G-.*")

        def _create_db_class(_tb_name):
            class MyCasbinPolicy(casbin_sqlalchemy_adapter.adapter.Base):
                __tablename__ = _tb_name
                id = Column(Integer, primary_key=True)
                ptype = Column(String(50))
                v0 = Column(String(50))
                v1 = Column(String(50))
                v2 = Column(String(50))
                v3 = Column(String(50))
                v4 = Column(String(50))
                v5 = Column(String(50))

                def __str__(self):
                    arr = [self.ptype]
                    for v in (self.v0, self.v1, self.v2, self.v3, self.v4, self.v5):
                        if v is None:
                            break
                        arr.append(v)
                    return ", ".join(arr)

                def __repr__(self):
                    return '<CasbinRule {}: "{}">'.format(self.id, str(self))

            return MyCasbinPolicy

        self._adapter = casbin_sqlalchemy_adapter.Adapter(connect_str, db_class=_create_db_class(info['tb']))
        self._enforce = casbin.SyncedEnforcer(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "../config_casbin_model_rbac.conf"),
            self._adapter)
        # self._enforce.start_auto_load_policy(1)  # auto load
        self._logger = logger
        self._info = info
        self._reload_channal_name = "__MYFRAME_CASBIN_RELOAD_SIGNAL"

    def set_auto_reload(self, service_redis: ServiceRedis):
        """casbin配置更新

        开启线程，订阅redis channel，发生变化后更新数据。

        Args:
            service_redis: ServiceRedis对象

        """

        self._service_redis = service_redis
        t = threading.Thread(target=self._thread_reload_policy)
        t.start()

    def _thread_reload_policy(self):
        self._logger.info("start casbin reload threading")
        rc = redis.Redis(connection_pool=self._service_redis.pool, decode_responses=True)
        ps = rc.pubsub()
        ps.subscribe(self._reload_channal_name)
        while True:
            item = ps.get_message()
            if item:
                if item['type'] == "message":
                    try:
                        if item['data'].decode('utf-8') == 'reload':
                            self._enforce.load_policy()
                            self._logger.debug("casbin reload in pid=%s tid=%s" % (
                                os.getpid(), threading.current_thread().ident))
                    except Exception as e:
                        self._logger.warning("casbin reload error with e=%s" % str(e))
            time.sleep(1)

    def _is_role(self, role):
        if self._group_pat.search(role):
            return True
        else:
            raise Exception(f"role must start with G- not {role}")

    def get_roles_for_user(self, user):
        return self._enforce.get_roles_for_user(user)

    def get_users_for_role(self, role):
        return self._enforce.get_users_for_role(role)

    def get_policies_for_role(self, role):
        if self._is_role(role):
            return self._enforce.get_filtered_policy(0, role)

    def add_role_for_user(self, user, role):
        if self._group_pat.search(role):
            rst = self._enforce.add_role_for_user(user, role)
            with self._service_redis.with_conn() as rc:
                rc.publish(self._reload_channal_name, "reload")
            return rst
        else:
            raise Exception(f"role must start with G- not {role}")

    def delete_role_for_user(self, user, role):
        rst = self._enforce.delete_role_for_user(user, role)
        with self._service_redis.with_conn() as rc:
            rc.publish(self._reload_channal_name, "reload")
        return rst

    def add_policy(self, role, obj, act):
        if self._group_pat.search(role):
            rst = self._enforce.add_policy(role, obj, act)
            with self._service_redis.with_conn() as rc:
                rc.publish(self._reload_channal_name, "reload")
            return rst
        else:
            raise Exception(f"role must start with G- not {role}")

    def remove_policy(self, role, obj, act):
        rst = self._enforce.remove_policy(role, obj, act)
        with self._service_redis.with_conn() as rc:
            rc.publish(self._reload_channal_name, "reload")
        return rst

    def enforce(self, sub, obj, act):
        # self._enforce.load_policy()
        return self._enforce.enforce(sub, obj, act)

