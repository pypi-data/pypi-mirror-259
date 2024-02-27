# -*- coding: UTF-8 -*-
# apscheduler
import loguru
import pymysql
from DBUtils.PersistentDB import PersistentDB
from DBUtils.PooledDB import PooledDB

ENCODING_UTF8 = "utf8"
import functools


class db(object):

    def __init__(self, pool=None, **kwargs):
        if pool:
            self.pool = pool
        elif kwargs and len(kwargs) > 0:
            self.host = kwargs.get("host")
            self.user = kwargs.get("user")
            self.password = kwargs.get("password")
            self.db = kwargs.get("db")
            self.port = kwargs.get("port")
            self.is_threading = kwargs.get("is_threading")
            self.max_usage = kwargs.get("maxusage")
            self.pool = self.is_threading and PersistentDB(pymysql, host=self.host or "",
                                                           user=self.user or "",
                                                           passwd=self.password or "",
                                                           db=self.db or "",
                                                           port=self.port or 3306,
                                                           maxusage=self.max_usage or 50,
                                                           charset=ENCODING_UTF8,
                                                           # 自动提交事务 选择否
                                                           setsession=['SET AUTOCOMMIT = 0']) or PooledDB(pymysql,
                                                                                                          host=self.host or "",
                                                                                                          user=self.user or "",
                                                                                                          passwd=self.password or "",
                                                                                                          db=self.db or "",
                                                                                                          port=self.port or 3306,
                                                                                                          maxusage=self.max_usage or 50,
                                                                                                          charset=ENCODING_UTF8,
                                                                                                          # 自动提交事务 选择否
                                                                                                          setsession=[
                                                                                                              'SET AUTOCOMMIT = 0'])

    def select(self, sql, is_dict=True):
        conn = None
        cursor = None
        try:
            conn = self.pool.connection()
            cursor = is_dict and conn.cursor(pymysql.cursors.DictCursor) or conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            loguru.logger.exception(e)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    def select_one(self, sql, is_dict=True):
        conn = None
        cursor = None
        try:
            conn = self.pool.connection()
            cursor = is_dict and conn.cursor(pymysql.cursors.DictCursor) or conn.cursor()
            cursor.execute(sql)
            return cursor.fetchone()
        except Exception as e:
            loguru.logger.exception(e)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()


    def execute(self, sql, values=None, is_auto_commit=False):
        '''
            增 删 改 操作
        :param sql:  需要执行的sql
        :param values:  sql中需要填充的值
        :param is_auto_commit: 是否自动提交事务
        :return:
        '''
        conn = None
        cursor = None
        try:
            conn = self.pool.connection()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
        except Exception as e:
            loguru.logger.exception(e)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()


    def executemany(self, sql, values=None, is_auto_commit=False):
        '''
            增 删 改 操作
        :param sql:  需要执行的sql
        :param values:  sql中需要填充的值
        :param is_auto_commit: 是否自动提交事务
        :return:
        '''
        conn = None
        cursor = None
        try:
            conn = self.pool.connection()
            cursor = conn.cursor()
            cursor.executemany(sql, values)
            conn.commit()
        except Exception as e:
            loguru.logger.exception(e)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    def select_by_param(self, sql, values, is_dict=True):
        conn = None
        cursor = None
        try:
            conn = self.pool.connection()
            cursor = is_dict and conn.cursor(pymysql.cursors.DictCursor) or conn.cursor()
            cursor.execute(sql, values)
            return cursor.fetchall()
        except Exception as e:
            loguru.logger.exception(e)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    # 事务提交
    def commit(self, conn=None, cursor=None):
        if conn:
            # 提交事务
            conn.commit()
            # 关闭游标
            if cursor:
                cursor.close()

    def rollback(self, conn=None, cursor=None):
        if conn:
            conn.rollback()
            if cursor:
                cursor.close()


def Transactional(p):
    '''
        ** 事务注解
    :param p:   class @db 注意 链接设置不可是自动提交
    :return:
    '''

    def transactional(fn):
        def wrapper(*args, **kwargs):
            try:
                fn(*args, **kwargs)
            except Exception as e:
                raise Exception(e)

        return functools.update_wrapper(wrapper, fn)

    return transactional
