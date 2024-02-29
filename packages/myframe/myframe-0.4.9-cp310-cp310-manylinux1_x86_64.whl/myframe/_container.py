import logging
from contextvars import ContextVar
from dependency_injector import containers, providers
from myframe._config import FrameModelProject
from myframe.service.service_jwt import ServiceJwt
from myframe.service.service_mysql import ServiceMysql
from myframe.service.service_redis import ServiceRedis
from myframe.service.service_casbin import ServiceCasbin
from myframe.service.service_httpclient import ServiceHpptClient
from myframe.service.service_logger import service_init_logger
from myframe.service.service_cdn import ServiceCdn
from myframe import util    # 触发认证代码


def create_container(project_config: FrameModelProject):
    class _MyDeclarativeContainer(containers.DeclarativeContainer):
        """动态设置属性"""

    class Container(_MyDeclarativeContainer):
        config = providers.Configuration()

        # resource

        # 类似flask.g，和request同样的作用域，fastapi中需要在中间件中设置
        contextvar_g = providers.Resource(ContextVar, 'contextvar_g', default=None)

        logger = providers.Resource(
            service_init_logger,
            project_name=config.project_name,
            path_log=project_config.config.other['path_log'],
            level=logging.DEBUG,
            contextvar_g=contextvar_g,
            log_column_contextvar=project_config.config.other.get('log_column_contextvar', ''),
            log_column_msg=project_config.config.other.get('log_column_msg', ''),
        )

        def _check_class_attr(_class, _name):
            if hasattr(_class, _name):
                raise Exception(f"{_class.__name__} already has attr {_name}")

        # dynamic service
        services = project_config.config.services
        if services:
            for v in services:
                v = v.dict()
                _check_class_attr(_MyDeclarativeContainer, v['name'])
                if v['type'] == 'mysql':
                    setattr(
                        _MyDeclarativeContainer,
                        v['name'],
                        providers.ThreadSafeSingleton(ServiceMysql, logger=logger, connect_info=v['info']))
                elif v['type'] == 'redis':
                    setattr(
                        _MyDeclarativeContainer,
                        v['name'],
                        providers.ThreadSafeSingleton(ServiceRedis, connect_info=v['info']))
                # elif v['type'] == 'grpc_client':
                #    setattr(
                #        _MyDeclarativeContainer,
                #        v['name'],
                #        providers.ThreadSafeSingleton(
                #            ServiceGrpcClient, connect_info=v['info'], contextvar_g=contextvar_g, logger=logger)
                #    )
                elif v['type'] == 'cdn':
                    setattr(
                        _MyDeclarativeContainer,
                        v['name'],
                        providers.ThreadSafeSingleton(ServiceCdn, info=v['info'], logger=logger)
                    )
                elif v['type'] == 'http_client':
                    setattr(
                        _MyDeclarativeContainer,
                        v['name'],
                        providers.Factory(
                            ServiceHpptClient, connect_info=v['info'], contextvar_g=contextvar_g, logger=logger)
                    )
                elif v['type'] == 'jwt':
                    setattr(
                        _MyDeclarativeContainer,
                        v['name'],
                        providers.Factory(ServiceJwt, info=v['info'])
                    )
                #elif v['type'] == 'paramsign':
                #    setattr(
                #        _MyDeclarativeContainer,
                #        v['name'],
                #        providers.Factory(ServiceParamsign, info=v['info'])
                #    )
                elif v['type'] == 'casbin':
                    setattr(
                        _MyDeclarativeContainer,
                        v['name'],
                        providers.ThreadSafeSingleton(
                            ServiceCasbin,
                            info=v['info'],
                            logger=logger),

                    )

    container = Container()
    container.config.from_dict(project_config.config.dict())
    return container
