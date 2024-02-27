# -*- coding: UTF-8 -*-
__info__ = '''
    * 多进程工具 
'''

import datetime
import multiprocessing
import time


class multiprocess(object):
    '''
     * 进程池
    '''
    process_list = list()

    def __init__(self, processes_size=5):
        self.processes_size = processes_size
        self.pool = multiprocessing.Pool(processes=processes_size)

    def add(self, fn, *args):
        # 异步添加
        self.process_list.append(self.pool.apply_async(fn, args))

    def check_process(self):
        for process in self.process_list :
            if process.ready() :
                self.process_list.remove(process)

def test(name):
    time.sleep(1)
    print(f"{datetime.datetime.now()} - {name}")


if __name__ == '__main__':
    m = multiprocess()
    c = 0
    while True:
        m.add(test, f"process = {c}")
        c += 1
        if c > 10:
            break
    while True:
        print("runing ... ")
        m.check_process()
        time.sleep(0.5)
        c += 1
        m.add(test, f"process = {c}")
