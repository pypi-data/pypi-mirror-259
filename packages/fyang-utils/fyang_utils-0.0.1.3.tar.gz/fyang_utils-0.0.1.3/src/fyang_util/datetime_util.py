# -*- coding: UTF-8 -*-
import calendar
import datetime as _datetime
import time
from typing import Union

_py_info = '''
    * 时间处理工具
    * 关于时间工具 有需求可以提 封装方法以方便处理时间
'''
# 毫秒
MICROSECOND = "microsecond"
# 秒
SECOND = "second"
# 分钟
MINUTE = "minute"
# 小时
HOUR = "hour"
# 日
DAY = "day"
# 周
WEEK = "week"
# 月
MONTH = "month"
# 年
YEAR = "year"

DEFAULT_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

DATE_FORMAT = "%Y-%m-%d"

DATE_TIME_MICROSECOND = "%Y-%m-%d %H:%M:%S.%s"


# datetime 接口 提供获取 天 周 月 年的开始结束时间  to_string 功能 时间差 获取时间戳
class __datetime(_datetime.datetime):
    # 获取开始时间
    def day_start_time(self): ...

    # 获取结束时间
    def day_end_time(self): ...

    # 获取 当前时间的周开始时间
    def week_start_time(self): ...

    # 获取 当前时间的周结束时间
    def week_end_time(self): ...

    # 获取 当前时间的月开始时间
    def month_start_time(self): ...

    # 获取 当前时间的月结束时间
    def month_end_time(self): ...

    # 获取 当前时间的月结束时间
    def year_start_time(self): ...

    # 获取 当前时间的月结束时间
    def year_end_time(self): ...

    # 格式化时间
    def to_string(self): ...

    # 获取时间戳(到毫秒)
    def timestamp_microsecond(self): ...

    # 获取时间戳 毫秒位都为0
    def timestamp(self): ...

    def get_datetime(self, **kwargs: Union[type(dict)]):
        ...

    # 获取目标时间时间差 单位 秒
    def diff_time(self, _time, _type=SECOND):
        ...


class datetime(__datetime):

    # 获取开始时间
    @property
    def day_start_time(self):
        return self.replace(hour=0, minute=0, second=0, microsecond=0)

    # 获取结束时间
    @property
    def day_end_time(self):
        return self.replace(hour=23, minute=59, second=59, microsecond=999999)

    # 获取 当前时间的周开始时间
    @property
    def week_start_time(self):
        return self.replace(hour=0, minute=0, second=0, microsecond=0) - _datetime.timedelta(days=self.weekday())

    # 获取 当前时间的周结束时间
    @property
    def week_end_time(self):
        return self.replace(hour=23, minute=59, second=59, microsecond=999999) + _datetime.timedelta(6 - self.weekday())

    # 获取 当前时间的月开始时间
    @property
    def month_start_time(self):
        return self.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    # 获取 当前时间的月结束时间
    @property
    def month_end_time(self):
        return self.replace(day=calendar.monthrange(self.year, self.month)[1], hour=23, minute=59, second=59,
                            microsecond=999999)

    # 获取 当前时间的月结束时间
    @property
    def year_start_time(self):
        if not self:
            self.now()
        return self.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)

    # 获取 当前时间的月结束时间
    @property
    def year_end_time(self):
        return self.replace(month=12, day=31, hour=23, minute=59, second=59,
                            microsecond=999999)

    # 格式化时间
    @property
    def to_string(self):
        return self.strftime(DEFAULT_DATETIME_FORMAT)

    # 获取时间戳(到毫秒)
    @property
    def timestamp_microsecond(self):
        return int((time.mktime(self.timetuple()) * 1000000 + self.microsecond) / 1000)

    # 获取时间戳 毫秒位都为0
    @property
    def timestamp(self):
        return int(time.mktime(self.timetuple()) * 1000)

    # 获取时间差
    def get_datetime(self, **kwargs):
        _week = kwargs.get("week") or 0
        _day = kwargs.get("day") or 0
        _hour = kwargs.get("hour") or 0
        _minute = kwargs.get("minute") or 0
        _second = kwargs.get("second") or 0
        _millisecond = kwargs.get("milliseconds") or 0

        return self + _datetime.timedelta(weeks=_week, days=_day, hours=_hour, minutes=_minute, seconds=_second,
                                          milliseconds=_millisecond)

    # 获取目标时间时间差 单位 秒
    def diff_time(self, _time, _type=SECOND):
        diff = self - _time
        days = diff.days
        seconds = diff.seconds
        if _type == DAY:
            return days
        else:
            return 24 * 3600 * days + seconds

    # @classmethod
    # def now(cls, tz=None):
    #     "Construct a datetime from time.time() and optional time zone info."
    #     t = time.time()
    #     return cls.fromtimestamp(t, tz)

#
# if __name__ == '__main__':
#     t = datetime.now().day_end_time
#     y = datetime.now().day_start_time.diff_time("t")
#     # x = y.year_start_time
#     print(y)
