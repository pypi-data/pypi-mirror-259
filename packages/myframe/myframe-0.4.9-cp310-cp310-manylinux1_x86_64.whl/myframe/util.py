import sys
import json
import uuid
import time
import ntplib
import platform
import sqlalchemy
import datetime
import contextlib

import pandas as pd
import numpy as np

import os
import re

import jwt

from dateutil.parser import parse
from typing import List, Tuple, Dict, Optional, Union

__license = False


def _verify_license():
    """检测license

    windows系统默认位置为~/license-grsh.dat；linux默认位置为/etc/gtjaqh/license-grsh.dat

    """

    global __license

    if __license:
        return

    def _check_time():
        client = ntplib.NTPClient()
        r = None
        try:
            r = client.request('pool.ntp.org', port='ntp', version=4, timeout=1)
            r = r.tx_time
        except:
            pass

        if r:
            if abs(time.time() - r) > 60 * 60 * 24 * 10:
                raise Exception("check machine time")

    _check_time()

    _key = """
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE6Uf4LBheJZhocDcEMp0tu9Jt4Wkp
ROKxXYF+xu0AoPR/RI0EkgtTI8hEeNzB2j1YSZhcOhSUXvWxemzNJYSCQg==
-----END PUBLIC KEY-----    
        """
    try:
        if platform.platform().upper().startswith("WINDOWS"):
            license_filename = os.path.expanduser("~/license-grsh.dat")
        elif platform.platform().upper().startswith("LINUX"):
            license_filename = "/etc/gtjaqh/license-grsh.dat"
        else:
            raise Exception(f"unkown platform {platform.platform()}")
        unverified_license = open(license_filename, 'r').read()
        payload = jwt.decode(
            jwt=unverified_license,
            key=_key,
            verify=True,
            algorithms=["ES256"],
            audience="GOD",
            issuer="国泰君安期货",
            options={'require_exp': True, 'verify_exp': True, 'verify_iss': True, 'verify_aud': True}
        )
        sys.stdout.writelines("[frame模块]该软件由[{}]向[{}]渠道[{}]客户授权使用至[{}]\n".format(
            payload['iss'],
            payload['aud'],
            payload['sub'],
            datetime.datetime.fromtimestamp(payload['exp'])))

        __license = True
        return True
    except FileNotFoundError:
        sys.stderr.writelines("license文件缺失")
        sys.exit()
    except jwt.exceptions.DecodeError:
        sys.stderr.writelines("license格式错")
        sys.exit()
    except jwt.exceptions.InvalidIssuerError:
        sys.stderr.writelines("license签发错误")
        sys.exit()
    except jwt.exceptions.InvalidAudienceError:
        sys.stderr.writelines("license渠道错误")
        sys.exit()
    except jwt.exceptions.ExpiredSignatureError:
        sys.stderr.writelines("license已过期")
        sys.exit()
    except Exception as e:
        print(e)
        sys.stderr.writelines("license异常")
        sys.exit()


_verify_license()


class ExceptionAuthFailed(Exception):
    """认证"""


class Tool:
    @staticmethod
    def parse_date(date: str = None) -> Union[datetime.date, None]:
        """解析yyyymmdd字符串格式的日期

        Args:
            date: yyyymmdd格式的字符串，传入None时候，返回None

        Raises:
            当date格式不对报错
        """

        if date is None:
            return None

        pat = re.compile("^[0-9]{8}$$")
        if pat.match(date):
            try:
                return parse(date).date()
            except:
                raise Exception("failed parse date %s" % date)
        else:
            raise Exception("not vaild date %s" % date)

    @staticmethod
    def list2str(lst: [list, str]) -> str:
        if isinstance(lst, str):
            return "@" + lst
        return "@" + "|".join([str(__v) for __v in lst])

    @staticmethod
    def df2json(df: pd.DataFrame) -> str:
        """将df转换为json字符串"""

        def _tmp(x):
            x = x.to_dict()
            for k in x:
                x[k] = str(x[k])
            return x

        return json.dumps(list(map(lambda x: _tmp(x[1]), df.iterrows())))

    @staticmethod
    def df2list(df: pd.DataFrame) -> List:
        """将df转换为list"""

        df = df.fillna('')

        def _tmp(x):
            x = x.to_dict()
            for k in x:
                x[k] = str(x[k])
            return x

        return list(map(lambda x: _tmp(x[1]), df.iterrows()))

    @staticmethod
    def df_fill_to_end(df: pd.DataFrame, column: str):
        df = df.copy(deep=True)
        _date = df[df[column].notnull()].iloc[-1].name
        _date_pos = df.index.get_loc(_date)
        df[column].fillna(method='ffill', inplace=True)
        if _date_pos < len(df):
            df[column].iloc[_date_pos + 1:] = np.nan
        return df

    @staticmethod
    def orm_object_to_jsonable_dict(obj):
        return {str(c.key): str(getattr(obj, c.key)) for c in sqlalchemy.inspect(obj).mapper.column_attrs}

    @staticmethod
    def make_jsonable(item):
        if isinstance(item, (datetime.date, datetime.datetime)):
            return str(item)
        else:
            return item

    @staticmethod
    def url_join(lst: List[str]) -> str:
        return '/'.join(lst).replace("///", "/").replace('//', '/').replace(':/', '://')

    @staticmethod
    def node_menu(data: List[Dict], path_column_name: str = 'path', name_column_name: str = 'name'):
        class _Node(dict):
            def __init__(self, _name, _id):
                self['node_name'] = _name
                self['node_id'] = "/" + _id
                self['children'] = []

        def _find_node(_node_list, _name, _id):
            for _node in _node_list:
                if _node['node_name'] == _name:
                    return _node
            _node = _Node(_name, _id)
            _node_list.append(_node)
            return _node

        menu_node_list = []
        for item in data:
            path = [v for v in item[path_column_name].split("/") if len(v) > 0]

            # 初始化&找到node
            children_node_list = menu_node_list
            for i, name in enumerate(path):
                node = _find_node(children_node_list, name, "/".join(path[:(i + 1)]))
                children_node_list = node['children']

            item['node_name'] = item[name_column_name]
            item['node_id'] = str(uuid.uuid4())
            node['children'].append(item)

        return menu_node_list

    @contextlib.contextmanager
    def work_in_dir(dirname=None):
        cur_dir = os.getcwd()
        try:
            if dirname is not None:
                os.chdir(dirname)
            yield
        finally:
            os.chdir(cur_dir)

    @staticmethod
    def is_uuid(value: str):
        try:
            uuid.UUID(str(value))
            return True
        except ValueError:
            return False
        # pattern = re.compile('^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[8-9a-b][0-9a-f]{3}-[0-9a-f]{12}$')
        # match = pattern.match(value)
        # if match:
        #    return True
        # else:
        #    return False
