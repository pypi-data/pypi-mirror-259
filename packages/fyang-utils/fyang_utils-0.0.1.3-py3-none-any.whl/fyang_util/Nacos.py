# -*- coding: UTF-8 -*-
import configparser
import os
import sys
import time

from nacos import NacosClient
import loguru
from apscheduler.schedulers.background import BackgroundScheduler

ENCODING_UTF_8 = "utf-8"
b = BackgroundScheduler()


def load(_env=None, file_path = "./config.ini" , listener_enable=False, interval=300, _config: configparser.ConfigParser = None):
    '''
        param _env 环境
        param file_path 需要保存的配置文件地址
        param listener_enable 是否需要监听配置
        param interval 刷新配置间隔 单位秒 但这只会修改 配置文件内容
        param _config 配置 ，如果不为空，会将配置刷进来

        外面需要有配置文件 NacosConfig-{环境}.ini
        例如，测试环境 NacosConfig-test.ini
             本地环境 NacosConfig-dev.ini
             线上环境 NacosConfig-prod.ini
        配置内容：
        [nacos]
        data_id=duyan-py3.ini
        group =duyan-py3
        namespace =e6a4b569-ec61-4494-9083-1f13502c06ed
        server_addr=10.72.147.56:8848
        username =chunyang.wang
        password =*******

        启动的时候 需要带上参数 @{env} 其中{env} 就是响应环境配置文件的后缀
            例如 ： 测试环境 配置文件为 NacosConfig-test.ini ， 启动项目 python3 your_project_name.py @test


        *** 注意 如果配置文件被多个脚本同时使用，可以只在其中一个脚本中使用本工具获取配置 刷新配置等操作 ，
        *** 其他脚本可以直接使用这个脚本获取的配置，不必重复在每个脚本中使用 尤其是监听功能
        *** 不推荐使用监听功能

    '''
    argvs = sys.argv
    if _env:
        env = _env or 'test'
    else:
        env = 'test'  # default test
        for var in argvs:
            if var.startswith("@"):
                env = var[1:]
    python_name = argvs[0]
    config_path = "./NacosConfig-%s.ini"
    config_path = config_path % env
    loguru.logger.info(f"项目[{python_name}]启动，环境[{env}],获取配置文件[{config_path}]")
    if config_path is None or not os.path.exists(config_path):
        raise Exception(f"配置文件[{config_path or 'None'}]不存在")
    config = configparser.ConfigParser()
    config.read(config_path, ENCODING_UTF_8)
    data_id = config.get('nacos', 'data_id')
    group = config.get('nacos', 'group')
    namespace = config.get('nacos', 'namespace')
    server_addr = config.get('nacos', 'server_addr')
    username = config.get('nacos', 'username')
    password = config.get('nacos', 'password')
    loguru.logger.debug("配置文件:\n"
                        f"    *  data_id:{data_id}\n"
                        f"    *  group:{group}\n"
                        f"    *  namespace:{namespace}\n"
                        f"    *  server_addr:{server_addr}\n"
                        f"    *  username:{username}\n"
                        f"    *  password:{password and len(password) and '***********' or 'None'}\n")

    client = NacosClient(server_addr, namespace=namespace, username=username, password=password)
    config = client.get_config(data_id, group)
    loguru.logger.debug(f"获取到配置 \n{config}")
    with open(file_path or './config.ini', "w+") as file:
        file.write(config)
    loguru.logger.info("配置加载完成")
    if _config:
        _config.read("./config.ini", ENCODING_UTF_8)
    if listener_enable:
        b.add_job(load, 'interval', seconds=interval, args=(env, file_path ,False, 300, _config))
        b.start()


if __name__ == '__main__':
    '''
        demo 
            初始化配置 并每隔 5 秒刷新一次配置
    '''
    # 创建配置
    c = configparser.ConfigParser()
    # 开启了 刷新配置文件
    load(listener_enable=True , interval=5, _config=c)
    while True :
        time.sleep(4)
        # 观察配置文件的变动 如果 nacos 变化 这里是否会变化
        print(c.get('mysql' , 'duyanHost'))
