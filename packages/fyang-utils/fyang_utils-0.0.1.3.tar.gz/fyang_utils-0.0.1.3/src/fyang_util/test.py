import unittest
from datetime import date, datetime

from duyan_util import datetime_util
from duyan_util import mongo_util
from duyan_util import mysql_util
from duyan_util import common_utils
from duyan_util.common_utils import DataMoveBase
# 从mysql同步到mysql 例子
from duyan_util.kafka_util import KafkaDataConsumer
from pymongo import ReplaceOne


class BillLogDataMove(DataMoveBase):

    def __init__(self, local_db, target_db, access_db, default_start_primary_id=None):
        super().__init__(platform=1,
                         task_sign='cti_bill_log_to_new_mysql',
                         primary_key_name='id',
                         local_db=local_db,
                         target_db=target_db,
                         access_db=access_db,
                         table_name='bill_log',
                         target_table_name='bill_log',
                         is_over_run=False,
                         move_type=self.MYSQL_TO_MYSQL,
                         default_start_primary_id=default_start_primary_id)

    def build_data(self, data):
        """
        数据构建
        """
        return [
            data.get('id'),
            data.get('type'),
            data.get('sub_type'),
            data.get('fee'),
            data.get('target_id'),
            data.get('parent_id'),
            data.get('org_id'),
            data.get('team_id'),
            data.get('agent_org_id'),
            data.get('call_minute'),
            data.get('left_amount'),
            data.get('data'),
            data.get('status'),
            data.get('created_time').strftime(datetime_util.DEFAULT_DATETIME_FORMAT),
            data.get('last_updated_time').strftime(datetime_util.DEFAULT_DATETIME_FORMAT),
        ]

    def insert_data(self, insert_values: list, insert_parmary_ids: list):
        """
        数据插入
        """
        sql = "INSERT INTO `cti`.`bill_log`(`id`, `type`, `sub_type`, `fee`, `target_id`, `parent_id`, `org_id`, `team_id`, `agent_org_id`, `call_minute`, `left_amount`, `data`, `status`, `created_time`, `last_updated_time`) " \
              "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        self.target_db.executemany(sql, insert_values)


# 从mysql同步到mongo 例子
class BillLogDataMoveMongo(DataMoveBase):

    def __init__(self, local_db, target_db, access_db, kafka_consumer=None, default_start_primary_id=None):
        super().__init__(platform=1,
                         task_sign='cti_bill_log_to_new_mysql',
                         primary_key_name='id',
                         local_db=local_db,
                         target_db=target_db,
                         access_db=access_db,
                         table_name='bill_log',
                         target_table_name='bill_log',
                         is_over_run=False,
                         move_type=self.MYSQL_TO_MONGO,
                         kafka_consumer=kafka_consumer,
                         default_start_primary_id=default_start_primary_id)

    def build_data(self, data):
        """
        数据构建
        """
        bill_log_mongo = BillLogMongoBuilder.build_document(data)
        bill_log_mongo_rp = ReplaceOne(filter={'id': data.get('id')}, replacement=bill_log_mongo, upsert=True)
        return bill_log_mongo_rp

    def insert_data(self, insert_values: list, insert_parmary_ids: list):
        """
        数据插入
        """
        self.target_db.table.bulk_write(insert_values)

    def increment_data_operation(self, primary_key_value, bin_log_type, bin_log_record):
        """
        增量同步自定义数据处理
        :param primary_key_value:
        :param bin_log_type:
        :param bin_log_record:
        :return:
        """
        if bin_log_type in ("INSERT", "UPDATE"):
            bill_log_mongo = BillLogMongoBuilder.build_document(bin_log_record)
            self.target_db.table.replace_one({'id': int(primary_key_value)}, bill_log_mongo)
        if bin_log_type == "DELETE":
            self.target_db.table.delete_one({'id': int(primary_key_value)})


class BillLogMongoBuilder:

    @staticmethod
    def build_document(bill_log):
        bill_log_mongo = dict()
        bill_log_mongo['id'] = int(bill_log.get('id'))
        bill_log_mongo['type'] = bill_log.get('type')
        bill_log_mongo['sub_type'] = BillLogMongoBuilder.get_int(bill_log.get('sub_type'))  # int类型
        bill_log_mongo['fee'] = BillLogMongoBuilder.get_int(bill_log.get('fee'))
        bill_log_mongo['target_id'] = BillLogMongoBuilder.get_int(bill_log.get('target_id'))
        bill_log_mongo['parent_id'] = BillLogMongoBuilder.get_int(bill_log.get('parent_id'))
        bill_log_mongo['org_id'] = BillLogMongoBuilder.get_int(bill_log.get('org_id'))
        bill_log_mongo['team_id'] = BillLogMongoBuilder.get_int(bill_log.get('team_id'))
        bill_log_mongo['agent_org_id'] = BillLogMongoBuilder.get_int(bill_log.get('agent_org_id'))
        bill_log_mongo['call_minute'] = BillLogMongoBuilder.get_int(bill_log.get('call_minute'))
        bill_log_mongo['left_amount'] = BillLogMongoBuilder.get_int(bill_log.get('left_amount'))
        bill_log_mongo['data'] = bill_log.get('data')
        bill_log_mongo['status'] = BillLogMongoBuilder.get_int(bill_log.get('status'))
        bill_log_mongo['created_time'] = BillLogMongoBuilder.get_time(bill_log.get('created_time'))  # 时间类型 mongo存储时用
        bill_log_mongo['last_updated_time'] = BillLogMongoBuilder.get_time(bill_log.get('last_updated_time'))
        return bill_log_mongo

    @staticmethod
    def get_int(t):
        if t is None:
            return None
        return int(t)

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
            return t.strftime(datetime_util.DEFAULT_DATETIME_FORMAT)
        if isinstance(t, int):
            tmp = datetime.fromtimestamp(t / 1000).strftime(datetime_util.DEFAULT_DATETIME_FORMAT)
        else:
            tmp = str(t)
        if 19 > len(tmp) >= 10:
            return datetime.strptime(tmp, datetime_util.DEFAULT_DATETIME_FORMAT)
        elif len(tmp) > 19:
            tmp = tmp[0:19]
        return tmp


class DataMoveObjTest(unittest.TestCase):

    @unittest.skip
    def test_data_move_obj(self):
        """
        mysql 到 mysql 全量
        """
        local_db = mysql_util.db(host='10.70.110.229', port=3306, db='cti', user='duyan', password='1234QWer')
        target_db = mysql_util.db(host='localhost', port=3306, db='cti', user='root', password='12345678')
        dm = BillLogDataMove(local_db=local_db, target_db=target_db, access_db=target_db,
                             default_start_primary_id=10160055)
        dm.full_data_sync()  # 全量同步

    @unittest.skip
    def test_date_check_day(self):
        """
        mysql 到 mysql 按日数据核对
        """
        local_db = mysql_util.db(host='10.70.110.229', port=3306, db='cti', user='duyan', password='1234QWer')
        target_db = mysql_util.db(host='localhost', port=3306, db='cti', user='root', password='12345678')
        dm = BillLogDataMove(local_db=local_db, target_db=target_db, access_db=target_db)
        dm.check_data_daily(date(year=2021, month=12, day=3))  # 按照日check

    @unittest.skip
    def test_data_move_obj_mongo(self):
        """
        mysql 到 mongo 全量
        """
        local_db = mysql_util.db(host='10.70.110.229', port=3306, db='cti', user='duyan', password='1234QWer')
        target_db = mongo_util.mongo_client(host='localhost', db='cti', table='bill_log')
        access_db = mysql_util.db(host='localhost', port=3306, db='cti', user='root', password='12345678')
        dm = BillLogDataMoveMongo(local_db=local_db, target_db=target_db, access_db=access_db,
                                  default_start_primary_id=10099178)
        dm.full_data_sync()

    @unittest.skip
    def test_date_check_day_mongo(self):
        """
        mysql 到 mongo 按日数据核对
        """
        local_db = mysql_util.db(host='10.70.110.229', port=3306, db='cti', user='duyan', password='1234QWer')
        target_db = mongo_util.mongo_client(host='localhost', db='cti', table='bill_log')
        access_db = mysql_util.db(host='localhost', port=3306, db='cti', user='root', password='12345678')
        dm = BillLogDataMoveMongo(local_db=local_db, target_db=target_db, access_db=access_db)
        dm.check_data_daily()

    @unittest.skip
    def test_increment_data_sync_once_mongo(self):
        """
        mysql 到 mongo 按日数据核对
        """
        local_db = mysql_util.db(host='10.70.110.229', port=3306, db='cti', user='duyan', password='1234QWer')
        target_db = mongo_util.mongo_client(host='localhost', db='cti', table='bill_log')
        access_db = mysql_util.db(host='localhost', port=3306, db='cti', user='root', password='12345678')
        consumer = KafkaDataConsumer(bootstrap_servers=['10.82.29.30:9092'],
                                     group_id='duyan_cti_bill_log_demo', topic_name='duyan_cti_bill_log',
                                     max_poll_records=10)
        dm = BillLogDataMoveMongo(local_db=local_db, target_db=target_db, access_db=access_db, kafka_consumer=consumer)
        dm.increment_data_sync()


class CommonUtilTest(unittest.TestCase):

    @unittest.skip
    def test_get_pid_by_process_name(self):
        print(common_utils.get_pid_by_process_name('python'))

    @unittest.skip
    def test_get_local_ipv4_ip(self):
        print(common_utils.get_local_ipv4_ip())

    @unittest.skip
    def test_get_encrypt_phone(self):
        print(common_utils.get_encrypt_phone('13164684503'))

    @unittest.skip
    def test_get_uuid(self):
        print(common_utils.get_uuid())

    @unittest.skip
    def test_generate_html(self):
        param = {'title': '测试', 'content': '你好啊！'}
        print(common_utils.generate_html('/Users/menghaowu/IdeaProjects/duyan-common/template', 'test.html', param))

    @unittest.skip
    def test_html_to_pdf(self):
        param = {'title': '测试', 'content': '你好啊！'}
        html = common_utils.generate_html('/Users/menghaowu/IdeaProjects/duyan-common/template', 'test.html', param)
        buffer = common_utils.html_to_pdf(html)
        with open('/Users/menghaowu/IdeaProjects/duyan-common/template/test.pdf', 'wb') as file:
            file.write(buffer)

    @unittest.skip
    def test_get_bytes_md5(self):
        path = '/Users/menghaowu/IdeaProjects/duyan-common/template/test.pdf'
        with open(path, 'rb') as file:
            print(common_utils.get_bytes_md5(file.read()))

    @unittest.skip
    def test_get_file_md5_sub(self):
        path = '/Users/menghaowu/IdeaProjects/duyan-common/template/test.pdf'
        print(common_utils.get_file_md5_sub(path))

    @unittest.skip
    def test_get_file_md5(self):
        path = '/Users/menghaowu/IdeaProjects/duyan-common/template/test.pdf'
        print(common_utils.get_file_md5(path))

    @unittest.skip
    def test_upload_to_oss_bytes(self):
        oss_util = common_utils.OssUtil(
            end_point='oss-cn-hangzhou.aliyuncs.com',
            access_key_id='LTAI4GFAeToJVw9E8eoLK8Wu',
            access_key_secret='Vpgar6tDmE3bmiCNrL0G5s8HCmzBfB',
            bucket_name='duyan-record-download')
        path = '/Users/menghaowu/IdeaProjects/duyan-common/template/test.pdf'
        with open(path, 'rb') as file:
            print(oss_util.upload_to_oss_bytes(file.read(), 'test.pdf'))

    @unittest.skip
    def test_upload_to_oss_file_name(self):
        oss_util = common_utils.OssUtil(
            end_point='oss-cn-hangzhou.aliyuncs.com',
            access_key_id='LTAI4GFAeToJVw9E8eoLK8Wu',
            access_key_secret='Vpgar6tDmE3bmiCNrL0G5s8HCmzBfB',
            bucket_name='duyan-record-download')
        path = '/Users/menghaowu/IdeaProjects/duyan-common/template/test.pdf'
        print(oss_util.upload_to_oss_by_file_path(path, 'test.pdf'))

    @unittest.skip
    def test_upload_to_oss_by_path(self):
        oss_util = common_utils.OssUtil(
            end_point='oss-cn-hangzhou.aliyuncs.com',
            access_key_id='LTAI4GFAeToJVw9E8eoLK8Wu',
            access_key_secret='Vpgar6tDmE3bmiCNrL0G5s8HCmzBfB',
            bucket_name='duyan-record-download')
        path = '/Users/menghaowu/IdeaProjects/duyan-common/template/test.pdf'
        print(oss_util.upload_to_oss_by_part(path, 'test.pdf'))

    def test_send_email(self):
        mail = common_utils.Mail(
            smtp_host='smtpdm.aliyun.com',
            smtp_port=465,
            host_mail='xxx.@xx.duyansoft.com',
            password='xxxx')
        mail.send_email(msg='测试', email=['xxxx@xxx.com'], subject='测试')


if __name__ == '__main__':
    CommonUtilTest.run()
