# -*- coding: UTF-8 -*-
import pymongo
import abc
from bson import Int64
from datetime import datetime, timedelta
import time

from duyan_util import config_util


class mongo_client(object):
    # 链接
    host = None
    # 库名
    db_name = None
    # 表名
    table_name = None
    # 客户端
    client = None
    # 库
    db = None
    # 表
    table = None

    def __init__(self, **kwargs):
        '''
        :param kwargs:
            * host :  链接地址
            * db :  数据库名
            * table : 表名
        '''
        if kwargs and len(kwargs) > 0:
            self.host = kwargs and kwargs.get("host") or None
            self.db_name = kwargs and kwargs.get("db") or None
            self.table_name = kwargs and kwargs.get("table") or None
            if self.host and self.db_name and self.table_name:
                self.client = pymongo.MongoClient(self.host)
                self.db = self.client.get_database(self.db_name)
                self.table = self.db.get_collection(self.table_name)
        else:
            # 如果是空的 用默认的
            config = config_util.config_obj("./config.ini")
            self.switch(config.mongo_host, config.mongo_db, config.mongo_table_name)

    def switch(self, host=None, db_name=None, table_name=None):
        '''
        :param host:  转换链接
        :param db_name: 转换库
        :param table_name: 转换表
        :return:
        '''
        if host:
            self.host = host
            self.client = pymongo.MongoClient(self.host)
            self.db_name = db_name
            self.table_name = table_name
            self.db = None
            self.table = None
        if db_name:
            self.db_name = db_name
            if self.client is None:
                raise Exception("客户端没有初始化")
            self.db = self.client.get_database(self.db_name)
            self.table_name = table_name
            self.table = None
        if table_name:
            self.table_name = table_name
            if self.db is None:
                raise Exception("没有初始化库")
            self.table = self.db.get_collection(self.table_name)


class BasicDBObject(dict):
    EQUALS = "$eq"
    NOT_EQUALS = "$ne"
    GREATER_THEN = "$gt"
    GREATER_THEN_EQUALS = "$gte"
    LESS_THEN = "$lt"
    LESS_THEN_EQUALS = "$lte"
    REGEX = "$regex"
    IN = "$in"
    NOT_IN = "$nin"
    MATCH = "$match"
    GROUP = "$group"
    SUM = "$sum"
    EXISTS = "$exists"

    @staticmethod
    def field_value_key(field_name):
        return f"${field_name}"

    def eq(self, key: str, value):
        '''
            等于
        '''
        return self.put(key, {self.EQUALS: value})

    def ne(self, key: str, value):
        '''
            不等于
        '''
        return self.put(key, {self.NOT_EQUALS: value})

    def gt(self, key, value):
        '''
            大于
        '''
        return self.put(key, {self.GREATER_THEN: value})

    def gte(self, key, value):
        '''
            大于等于
        '''
        return self.put(key, {self.GREATER_THEN_EQUALS: value})

    def lt(self, key, value):
        '''
            小于
        '''
        return self.put(key, {self.LESS_THEN: value})

    def lte(self, key, value):
        '''
            小于等于
        '''
        return self.put(key, {self.LESS_THEN_EQUALS: value})

    def between(self, key, min_value, max_value):
        return self.put(key, {self.GREATER_THEN_EQUALS: min_value, self.LESS_THEN_EQUALS: max_value})

    def range(self, key, min_value, max_value, include_min=False, include_max=False):
        '''
            范围查询 ， 默认前后不包括
        '''
        return self.put(key,
                        {include_min and self.GREATER_THEN_EQUALS or self.GREATER_THEN: min_value,
                         include_max and self.LESS_THEN_EQUALS or self.LESS_THEN: max_value})

    def like(self, key, regex_value):
        return self.put(key, {self.REGEX: regex_value})

    def in_(self, key, value: list):
        return self.put(key, {self.IN: value})

    def not_in(self, key, value: list):
        return self.put(key, {self.NOT_IN: value})

    def sum(self, name, field_name):
        return self.put(name, {self.SUM: field_name})

    def exists(self, key, v: bool):
        if not isinstance(v, bool):
            raise Exception("exists 仅支持 bool 类型的判断")
        return self.put(key, {self.EXISTS: v})

    def match(self, query):
        return self.put(self.MATCH, query)

    def group(self, aggregate):
        return self.put(self.GROUP, aggregate)

    def put(self, key, value):
        if isinstance(key, bytes):
            key = str(key, encoding='utf-8')
        key = str(key)
        if key in self.keys():
            raise Exception(f"字段{key}条件已存在")
        self[key] = value
        return self

    def select_fields(self, *show_fields):
        '''
                只查询特定的字段
        '''
        if show_fields:
            show_query = dict()
            for field in show_fields:
                show_query[field] = 1
            return self, show_query
        return self


class MongoDataBuilder(abc.ABC):
    """
    mongo数据构建器
    """

    @abc.abstractstaticmethod
    def build_document(data):
        ...

    @staticmethod
    def get_int(t):
        if t is None:
            return None
        return int(t)

    @staticmethod
    def get_int64(value):
        if value is None:
            return None
        return Int64(int(value))

    @staticmethod
    def get_float(t):
        if t is None:
            return None
        return float(t)

    @staticmethod
    def get_time(t):
        if not t:
            return None
        if isinstance(t, datetime):
            return t.strftime(DataUtil.DEFAULT_FORMAT)
        if isinstance(t, int):
            tmp = DataUtil.get_time(t / 1000)
        else:
            tmp = str(t)
        if 19 > len(tmp) >= 10:
            return datetime.strptime(tmp, DataUtil.DATE_FORMAT)
        elif len(tmp) > 19:
            tmp = tmp[0:19]
        return tmp

    @staticmethod
    def get_str(t):
        if t is None:
            return None
        return str(t)


class DataUtil(object):
    DEFAULT_FORMAT = "%Y-%m-%d %H:%M:%S"
    DATE_FORMAT = "%Y%m%d"

    @staticmethod
    def get_time(t: [float, int], fmt=DEFAULT_FORMAT):
        return time.strftime(fmt, time.localtime(t))

    @classmethod
    def get_time_after_format(cls, after_days, t=None, fmt=DEFAULT_FORMAT):
        after_day = cls.get_time_after(after_days, t)
        return after_day.strftime(fmt)

    @staticmethod
    def get_time_after(after_days, t=None) -> datetime:
        if not t:
            t = datetime.now()
        return t + timedelta(days=after_days)

    if __name__ == '__main__':
        sql = BasicDBObject()
        sql.eq("a", 123).gt(1, 3).ne("b", 32).between("c", 1, 5).exists("d", False).in_("agent", [1, 2, 34, 5]).range(
            "call_time", "2021", "2022", True, False)

        print(str(sql.select_fields("org_id", "team_id")))
