# -*- coding: UTF-8 -*-
import configparser
import os

import pymongo
import pymysql
import redis as redis
from DBUtils.PersistentDB import PersistentDB
from DBUtils.PooledDB import PooledDB
from loguru import logger
from clickhouse_driver import Client

ENCODING_UTF_8 = "utf-8"
ENCODING_UTF8 = "utf8"
SMS = 'sms'
CTI = 'cti'
ANMI = 'anmi'
CDR = "cdr"
_VALUE = "value"
# mysql key
CONFIG_MYSQL_SETTING_KEY = "mysql"
# redis key
CONFIG_REDIS_SETTING_KEY = "redis"
# mongo
COMFIG_MONGO_SETTING_KEY = "mongo"
# clickhouse
CONFIG_CLICK_HOUSE_KEY = "clickhouse"
# mongo 默认表名
DEFAULT_MONGO_TABLE_NAME = "call_log"
# 默认配置文件地址
DEFAULT_CONFIG_FILE_PATH = "./config.ini"
#
_py_info = '''
    * 度言配置类 现在一共三类 sms cti anmi 分别给 短信系统 度言呼叫平台 安米催收系统使用
    * 功能 封装配置 获取 数据库连接池 ，redis 链接， mongo 连接 ，clickhouse ， hologress ，发送邮件 ，以及一些基础配置（基础配置需要通过 get_value 方法使用获取）
'''

_UNSET = object()


def singleton(cls, *args, **kwargs):
    instances = {}

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


# 度言专用config
@singleton
class config_obj(object):
    config_path = None
    config = None

    # mysql 配置
    mysql_host = {SMS: "sms_host", CTI: "duyanHost", ANMI: "anmiHost", CDR: "cdrHost", _VALUE: None}
    mysql_user = {SMS: "sms_user", CTI: "duyanUser", ANMI: "anmiUser", CDR: "cdrUser", _VALUE: None}
    mysql_password = {SMS: "sms_password", CTI: "duyanPassword", ANMI: "cdrPassword", CDR: "cdrDB", _VALUE: None}
    mysql_port = {SMS: "sms_port", CTI: "duyanPort", ANMI: "anmiPort", CDR: "cdrPort", _VALUE: 3306}
    mysql_name = {SMS: "sms_db_name", CTI: "duyanDB", ANMI: "anmiDB", CDR: "cdrDB", _VALUE: None}
    mysq_pools = {SMS: None, CTI: None, ANMI: None, CDR: None}
    # redis 配置
    redis_host = {SMS: "sms_host", CTI: "duyanHost", ANMI: "anmiHost", _VALUE: None}
    redis_port = {SMS: "sms_port", CTI: "duyanPort", ANMI: "anmiPort", _VALUE: 6379}
    redis_db = {SMS: "sms_db", CTI: "duyanDB", ANMI: "anmiDB", _VALUE: 0}
    redis_password = {SMS: "sms_possword", CTI: "duyanPassword", ANMI: "anmiPassword", _VALUE: None}
    redis_pools = {SMS: None, CTI: None, ANMI: None, CDR: None}

    # mongo 配置
    mongo_host = None
    mongo_db = None
    mongo_table_name = DEFAULT_MONGO_TABLE_NAME
    mongoDB = None

    # clickhouse 配置
    clickhouse_host = None
    clickhouse_database = None
    clickhouse_user = None
    clickhouse_password = None

    def __init__(self, file_path=DEFAULT_CONFIG_FILE_PATH, platform_name=CTI):
        if not os.path.exists(file_path):
            raise Exception(f"配置文件[{file_path}]不存在。")
        if not platform_name:
            raise Exception('环境参数不能为空')
        self.file_path = file_path
        self.config = configparser.ConfigParser()
        self.config.read(self.file_path, ENCODING_UTF_8)
        self.platform_name = platform_name
        if CTI == self.platform_name :
            self.load_file()

    def load_file(self):
        self.mysql_host[_VALUE] = self.get_value(CONFIG_MYSQL_SETTING_KEY, self.mysql_host.get(self.platform_name))
        self.mysql_user[_VALUE] = self.get_value(CONFIG_MYSQL_SETTING_KEY, self.mysql_user.get(self.platform_name))
        self.mysql_password[_VALUE] = self.get_value(CONFIG_MYSQL_SETTING_KEY,
                                                     self.mysql_password.get(self.platform_name))
        self.mysql_port[_VALUE] = int(
            self.get_value(CONFIG_MYSQL_SETTING_KEY, self.mysql_port.get(self.platform_name)) or 0)
        self.mysql_name[_VALUE] = self.get_value(CONFIG_MYSQL_SETTING_KEY, self.mysql_name.get(self.platform_name))
        self.redis_host[_VALUE] = self.get_value(CONFIG_REDIS_SETTING_KEY, self.redis_host.get(self.platform_name))
        self.redis_port[_VALUE] = self.get_value(CONFIG_REDIS_SETTING_KEY, self.redis_port.get(self.platform_name))
        self.redis_db[_VALUE] = self.get_value(CONFIG_REDIS_SETTING_KEY, self.redis_db.get(self.platform_name))
        self.redis_password[_VALUE] = self.get_value(CONFIG_REDIS_SETTING_KEY,
                                                     self.redis_password.get(self.platform_name))
        self.mongo_host = self.get_value(COMFIG_MONGO_SETTING_KEY, "host")
        self.mongo_db = self.get_value(COMFIG_MONGO_SETTING_KEY, "db")
        self.clickhouse_host = self.get_value(CONFIG_CLICK_HOUSE_KEY, "server_host")
        self.clickhouse_database = self.get_value(CONFIG_CLICK_HOUSE_KEY, "db")
        self.clickhouse_user = self.get_value(CONFIG_CLICK_HOUSE_KEY, "user")
        self.clickhouse_password = self.get_value(CONFIG_CLICK_HOUSE_KEY, "password")

    @logger.catch
    def get_value(self, key, field):
        if not self.config or not self.config.has_option(key, field):
            return None
        return self.config.get(key, field)

    @logger.catch
    def get_mysql_pool(self, is_threading=False):
        # if self.mysq_pools.get(self.platform_name):
        #     return self.mysq_pools.get(self.platform_name)
        _pool = is_threading and PersistentDB(pymysql, 5, host=self.mysql_host.get(_VALUE) or "",
                                              user=self.mysql_user.get(_VALUE) or "",
                                              passwd=self.mysql_password.get(_VALUE) or "",
                                              db=self.mysql_name.get(_VALUE) or "",
                                              port=self.mysql_port.get(_VALUE) or 3306,
                                              maxusage=50,
                                              charset=ENCODING_UTF8) or PooledDB(pymysql, 5,
                                                                                 host=self.mysql_host.get(_VALUE) or "",
                                                                                 user=self.mysql_user.get(_VALUE) or "",
                                                                                 passwd=self.mysql_password.get(
                                                                                     _VALUE) or "",
                                                                                 db=self.mysql_name.get(_VALUE) or "",
                                                                                 port=self.mysql_port.get(
                                                                                     _VALUE) or 3306,
                                                                                 maxusage=50,
                                                                                 charset=ENCODING_UTF8)
        self.mysq_pools[self.platform_name] = _pool
        return _pool

    @logger.catch
    def get_redis_pool(self):
        if self.redis_pools.get(self.platform_name):
            return self.redis_pools.get(self.platform_name)
        _pool = redis.ConnectionPool(host=self.redis_host.get(_VALUE),
                                     port=self.redis_port.get(_VALUE),
                                     password=self.redis_password.get(_VALUE),
                                     db=self.redis_db.get(_VALUE))
        self.redis_pools[self.platform_name] = _pool
        return _pool

    # 初始化mongo db
    @logger.catch
    def mongo_db_init(self):
        self.myclient = pymongo.MongoClient(self.mongo_host)
        self.mongoDB = self.myclient.get_database(name=self.mongo_db)

    # 获取表集合
    @logger.catch
    def get_mongo_collection(self, table_name=None):
        if not self.mongoDB:
            self.mongo_db_init()
        self.mongo_table_name = table_name or self.mongo_table_name
        return self.mongoDB.get_collection(self.mongo_table_name)

    # 转换环境 cti sms anmi
    def switch(self, platform_name):
        if self.platform_name == platform_name:
            return
        self.platform_name = platform_name
        self.load_file()

    # 获取 click house 连接
    @logger.catch
    def get_clickhouse_connect_engine(self):
        return Client(host=config['clickhouse']['server_host'], database=config['clickhouse']['db'],
                      user=config['clickhouse']['user'], password=config['clickhouse']['password'])

    def get_or_default(self, section, option, default_value):
        try:
            if not self.config.has_option(section, option):
                return default_value
            if isinstance(default_value, int):
                value = self.config.getint(section, option)
            elif isinstance(default_value, bool):
                value = self.config.getboolean(section, option)
            elif isinstance(default_value, float):
                value = self.config.getfloat(section, option)
            else:
                value = self.config.get(section, option)
            if value is None:
                return default_value
            return value
        except Exception as e:
            return default_value


# 通用型 未开发完成
class config(configparser.ConfigParser):
    def __init__(self, config_path):
        super().__init__()
        self.read(config_path, ENCODING_UTF_8)

    # 增加一个默认值
    def get(self, section, option, default_value=None, raw=False, vars=None, fallback=_UNSET):
        if self.has_option(section, option):
            value = super().get(section, option, raw=raw, vars=vars, fallback=fallback)
            if value is None:
                return default_value
            if default_value is not None:
                try:
                    if isinstance(default_value, int):
                        return int(value)
                    elif isinstance(default_value, bool):
                        return bool(value)
                    elif isinstance(default_value, float):
                        return float(value)
                    return value
                except Exception as e:
                    logger.error(e)
        return default_value
