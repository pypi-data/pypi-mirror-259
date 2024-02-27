# -*- coding: UTF-8 -*-
import datetime
import socket

import apscheduler.schedulers.blocking as b
import redis
from apscheduler.schedulers import base

BlockingScheduler = b.BlockingScheduler()


class ApschedulerManager(object):

    def __init__(self, redis_pool=None, max_count: int = 0 , timeout:int = 0 ):
        if not redis_pool:
            raise Exception("redis pool can't be none !")
        self.redis_pool = redis_pool
        # 获取计算机名称
        hostname = socket.gethostname()
        print(hostname)
        # 获取本机IP
        ip = socket.gethostbyname(hostname)
        self.redis_local_key = f"{hostname and str(hostname).replace('.', '_') or 'UNKONOWN_SERVER_NAME'}_{ip and str(ip).replace('.', '_') or 'UNKNOWN_SERVER_IP'}"
        print(self.redis_local_key)
        r = redis.Redis(connection_pool=self.redis_pool)
        # if not r.exists(self.redis_local_key) :



def schedulers_block(fn, type='interval', args=(), **kwargs):
    def run():
        BlockingScheduler.add_job(fn, 'interval', seconds=2, next_run_time=datetime.datetime.now())
        BlockingScheduler.start()
        if not BlockingScheduler.state == base.STATE_RUNNING:
            BlockingScheduler.start()
        print(111)

    return run


@schedulers_block
def x(z=None):
    if z:
        print(z)
    print(datetime.datetime.now())


if __name__ == '__main__':
    ApschedulerManager()
