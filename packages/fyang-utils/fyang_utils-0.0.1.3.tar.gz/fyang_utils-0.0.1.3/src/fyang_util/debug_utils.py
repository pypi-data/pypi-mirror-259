#!/usr/bin/python
# -*- coding: UTF-8 -*-
# fileName : debug_utils.py
# description : debug相关工具
# author : wmh
import time
from functools import wraps


def time_fn(fn):
    """
    方法执行时间装饰器 在方法上加 @time_fn 可查看方法执行时间 debug时可使用
    :param fn:
    :return:
    """
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print ("@timefn:" + fn.__name__ + " took " + str(t2 - t1) + " seconds")
        return result

    return measure_time