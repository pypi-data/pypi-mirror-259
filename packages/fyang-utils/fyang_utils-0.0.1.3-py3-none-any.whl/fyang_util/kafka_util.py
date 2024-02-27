#!/usr/bin/python
# -*- coding: UTF-8 -*-
# fileName : kafka_utils.py
# description : kafka工具
# author : wmh
import ssl
import time
from concurrent.futures import ThreadPoolExecutor

import loguru
from kafka import KafkaConsumer, KafkaProducer, TopicPartition, OffsetAndMetadata


class KafkaDataConsumer:

    def __init__(self, bootstrap_servers, group_id, topic_name, use_ssl=False, ca_cert_location=None,
                 sasl_plain_username=None, sasl_plain_password=None, session_timeout_ms=25000,
                 max_poll_records=100, auto_commit=True):
        # 配置
        self.__config = self.ConsumerConfig(bootstrap_servers, group_id, topic_name, use_ssl, ca_cert_location,
                                            sasl_plain_username, sasl_plain_password, session_timeout_ms,
                                            max_poll_records)
        self.__enable_auto_commit = auto_commit
        # 用于获取元信息
        self.__consumer_manager = KafkaConsumer(
            group_id=group_id,
            bootstrap_servers=bootstrap_servers,
            api_version=(0, 10, 0),
            session_timeout_ms=session_timeout_ms,
            max_poll_records=max_poll_records,
            fetch_max_bytes=1 * 1024 * 1024,
            enable_auto_commit=False
        )
        if use_ssl:
            ssl_context = ssl.create_default_context()
            ssl_context.verify_mode = ssl.CERT_REQUIRED
            ssl_context.check_hostname = False
            ssl_context.load_verify_locations(ca_cert_location)
            self.__consumer_manager.config['security_protocol'] = 'SASL_SSL'
            self.__consumer_manager.config['sasl_mechanism'] = 'PLAIN'
            self.__consumer_manager.config['sasl_plain_username'] = sasl_plain_username
            self.__consumer_manager.config['sasl_plain_password'] = sasl_plain_password

        # 获取当前消费者分配的分区
        partition_id_set = self.__consumer_manager.partitions_for_topic(self.__config.topic_name)
        if partition_id_set is None or len(partition_id_set) == 0:
            raise Exception("topic do not exists!")
        # 分区id列表
        self.__partition_ids = list(partition_id_set)
        # 初始化订阅partition信息
        self.__partitions = []
        for partition_id in partition_id_set:
            self.__partitions.append(TopicPartition(self.__config.topic_name, partition_id))

        # 初始化分区的partition信息
        self.__offsets = self.__get_init_partition_offset()
        # 初始化work节点
        self.__worker = self.__get_init_consumer_workers()
        # thead_exc
        self.__executor = ThreadPoolExecutor(max_workers=10, thread_name_prefix="KafkaDataConsumer_thread_pool")

    def __get_init_partition_offset(self):
        offsets = {}
        for partition in self.__partitions:
            # 从上次提交的消费位点开始消费
            offset_mate_data = self.__consumer_manager.committed(partition)
            # 如果获取不到则从头消费
            if offset_mate_data is None:
                partition_offset = self.__consumer_manager.beginning_offsets([partition])
                if partition_offset is None or len(partition_offset) == 0:
                    raise Exception(f"OffsetError: partition :{partition} , 无初始化消费位点")
                offset_mate_data = partition_offset.get(partition)
            if offset_mate_data is not None:
                if isinstance(offset_mate_data, OffsetAndMetadata):
                    offset = offset_mate_data.get(partition)
                    offsets[partition] = 0 if offset == 0 else offset + 1
                if isinstance(offset_mate_data, int):
                    offset = offset_mate_data
                    offsets[partition] = 0 if offset == 0 else offset + 1
                else:
                    raise Exception(f"TypeError: {type(offset_mate_data)} is not int or OffsetAndMetadata")
            loguru.logger.info(
                f"[topic:{self.__config.topic_name}],[group_id:{self.__config.group_id}],初始化消费位点信息,partition:{partition},  offset: {offset_mate_data}")
        return offsets

    def __get_init_consumer_workers(self):
        works = {}
        for partition in self.__partitions:
            work = self.ConsumerWorker(
                self.__config.bootstrap_servers,
                self.__config.group_id,
                self.__config.topic_name,
                partition,
                self.__config.use_ssl,
                self.__config.ca_cert_location,
                self.__config.sasl_plain_username,
                self.__config.sasl_plain_password,
                self.__config.session_timeout_ms,
                self.__config.max_poll_records,
                self.__enable_auto_commit
            )
            works[partition] = work
        return works

    def reset_offset(self, partition_id, offset):
        """
        重置消费的offset
        :param offset:
        :param partition_id:
        :return:
        """
        if partition_id not in self.__partition_ids:
            raise Exception(
                f"[topic:{self.__config.topic_name}],[group_id:{self.__config.group_id}],消费位点重置失败,partition_id : {partition_id} 不存在")
        # 初始化消费位点
        partition = TopicPartition(self.__config.topic_name, partition_id)
        self.__offsets[partition] = offset
        loguru.logger.info(
            f"[topic:{self.__config.topic_name}],[group_id:{self.__config.group_id}],消费位点重置成功:[{self.__offsets[partition]}]")

    def get_data(self):
        """
        获取最新的数据
        """
        features = []
        result_datas = []
        for partition in self.__partitions:
            worker = self.__worker.get(partition)
            feature = self.__executor.submit(worker.get_data, self.__offsets.get(partition))
            features.append(feature)
        # 获取结果
        for result in features:
            result_datas.extend(result.result())
        # 跟新最新的offset
        for worker_partition, this_worker in self.__worker.items():
            self.__offsets[worker_partition] = this_worker.offset
        return result_datas

    def get_message(self):
        """
        获取最新的消息
        """
        features = []
        result_message = []
        for partition in self.__partitions:
            worker = self.__worker.get(partition)
            feature = self.__executor.submit(worker.get_message, self.__offsets.get(partition))
            features.append(feature)
        # 获取结果
        for result in features:
            result_message.extend(result.result())
        # 跟新最新的offset
        for worker_partition, this_worker in self.__worker.items():
            self.__offsets[worker_partition] = this_worker.offset
        return result_message

    def subscribe(self, listener_fn, seconds=5):
        """
        订阅模式 每seconds时间拉一批数据
        :param listener_fn: 消费方法
        :param seconds: 时间
        :return:
        """
        while True:
            message_list = self.get_message()
            for message in message_list:
                listener_fn(message)
                if self.__enable_auto_commit:
                    self.commit(message.partition, message.offset)
            time.sleep(seconds)

    def commit(self, partition, offset):
        """
        手动提交消费
        :param partition:
        :param offset:
        :return:
        """
        topic_partition = TopicPartition(self.__config.topic_name, partition)
        self.__offsets[topic_partition] = offset + 1
        self.__worker.get(topic_partition).commit(offset)

    class ConsumerConfig:

        def __init__(self, bootstrap_servers, group_id, topic_name, use_ssl, ca_cert_location,
                     sasl_plain_username, sasl_plain_password, session_timeout_ms,
                     max_poll_records):
            self.bootstrap_servers = bootstrap_servers
            self.group_id = group_id
            self.topic_name = topic_name
            self.use_ssl = use_ssl
            self.ca_cert_location = ca_cert_location
            self.sasl_plain_username = sasl_plain_username
            self.sasl_plain_password = sasl_plain_password
            self.session_timeout_ms = session_timeout_ms
            self.max_poll_records = max_poll_records

    class ConsumerWorker:
        """
        kafka消费端集成
        """

        def __init__(self, bootstrap_servers, group_id, topic_name, partition, use_ssl=False, ca_cert_location=None,
                     sasl_plain_username=None, sasl_plain_password=None, session_timeout_ms=25000,
                     max_poll_records=1000, auto_commit=False):
            self.topic_name = topic_name
            self.group_id = group_id
            self.partition = partition
            self.consumer = KafkaConsumer(
                group_id=group_id,
                bootstrap_servers=bootstrap_servers,
                api_version=(0, 10, 0),
                session_timeout_ms=session_timeout_ms,
                max_poll_records=max_poll_records,
                fetch_max_bytes=1 * 1024 * 1024,
                enable_auto_commit=False
            )
            if use_ssl:
                ssl_context = ssl.create_default_context()
                ssl_context.verify_mode = ssl.CERT_REQUIRED
                ssl_context.check_hostname = False
                ssl_context.load_verify_locations(ca_cert_location)
                self.consumer.config['security_protocol'] = 'SASL_SSL'
                self.consumer.config['sasl_mechanism'] = 'PLAIN'
                self.consumer.config['sasl_plain_username'] = sasl_plain_username
                self.consumer.config['sasl_plain_password'] = sasl_plain_password
            self.consumer.assign([partition])
            self.enable_auto_commit = auto_commit
            loguru.logger.info(
                f"[topic:{self.topic_name}],[group_id:{self.group_id}], partition: [{self.partition}],worker初始化完成...")

        def get_data(self, offset=None):
            """
            获取队列数据
            :param offset: 指定消息起始的offset
            :return:
            """
            # 初始化消费位点
            self.reset_offset(offset)
            # 开始位点
            start_offset = self.offset
            # 数据
            data_list = []
            # 获取数据
            topic_records_map = self.consumer.poll(timeout_ms=9999)
            if topic_records_map is None or len(topic_records_map) == 0:
                # loguru.logger.info(f"[topic:{self.topic_name}],[group_id:{self.group_id}],已无新数据...")
                return []
            records = list(topic_records_map.get(self.partition))
            # 更新下一次消费位点
            if len(records) > 0:
                last_record = records[len(records) - 1]
                end_offset = last_record.offset
                # 提交最新的offset
                self.consumer.commit({self.partition: OffsetAndMetadata(end_offset, None)})
                self.offset = end_offset + 1
            else:
                end_offset = start_offset
            # 获取最终数据
            for data in records:
                data_list.append(bytes.decode(data.value, encoding='utf-8'))

            if self.offset > start_offset:
                loguru.logger.info(
                    f"[topic:{self.topic_name}],[group_id:{self.group_id}],获取数据成功,partition :[{self.partition}], start_off:{start_offset}, end_offset:{end_offset}")
            return data_list

        def get_message(self, offset=None):
            """
            获取队列原始message
            :param offset: 指定消息起始的offset
            :return:
            """
            # 初始化消费位点
            self.reset_offset(offset)
            # 开始位点
            start_offset = self.offset
            # 获取数据
            topic_records_map = self.consumer.poll(timeout_ms=9999)
            if topic_records_map is None or len(topic_records_map) == 0:
                # loguru.logger.info(f"[topic:{self.topic_name}],[group_id:{self.group_id}],已无新数据...")
                return []
            records = list(topic_records_map.get(self.partition))
            # 更新下一次消费位点
            if len(records) > 0:
                last_record = records[len(records) - 1]
                end_offset = last_record.offset
                # 提交最新的offset
                if self.enable_auto_commit:
                    self.consumer.commit({self.partition: OffsetAndMetadata(end_offset, None)})
                    self.offset = end_offset + 1
                loguru.logger.info(
                    f"[topic:{self.topic_name}],[group_id:{self.group_id}],获取数据成功,partition :[{self.partition}], start_off:{start_offset}, end_offset:{end_offset}")
            return records

        def reset_offset(self, offset):
            """
            重置消费的offset
            :param offset:
            :return:
            """
            # 初始化消费位点
            self.offset = offset
            self.consumer.seek(self.partition, self.offset)
            if offset != self.offset:
                loguru.logger.info(
                    f"[topic:{self.topic_name}],[group_id:{self.group_id}], partition: [{self.partition}], offset is reset to {self.offset}")

        def commit(self, offset: int):
            """
            手动提交
            :param offset:
            :return:
            """
            self.consumer.commit({self.partition: OffsetAndMetadata(offset, None)})
            self.offset = offset + 1


def test_send():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    for i in range(0, 1000):
        message = f"this is the {i}th message !"
        producer.send('test-topic', message.encode('utf-8'))


def test_consume():
    c = KafkaDataConsumer(bootstrap_servers=['10.82.29.30:9092'],
                          group_id='demo01', topic_name='duyan_cti_bill_log',
                          max_poll_records=10)

    print(c.get_data())


def test_subscribe():
    c = KafkaDataConsumer(bootstrap_servers=['10.82.29.30:9092'],
                          group_id='demo01', topic_name='duyan_cti_bill_log',
                          max_poll_records=10, auto_commit=False)
    # c.reset_offset(0, 200)
    # c.reset_offset(1, 200)
    # c.reset_offset(2, 200)
    # c.reset_offset(3, 200)
    # c.reset_offset(4, 200)
    # c.reset_offset(5, 200)
    # c.reset_offset(6, 200)
    # c.reset_offset(7, 200)
    # c.reset_offset(8, 200)
    # c.reset_offset(9, 200)

    def do_biz(message):
        print(message.topic, message.offset, message.partition)
        c.commit(message.partition, message.offset)

    c.subscribe(do_biz, seconds=1)


if __name__ == '__main__':
    # test_send()
    test_subscribe()
