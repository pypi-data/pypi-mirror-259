# -*- coding: UTF-8 -*-
import abc
import json
import os
import smtplib
import subprocess
import time
import uuid
import oss2
from hashlib import md5
from datetime import date, timedelta, datetime
from io import BytesIO
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import loguru
import netifaces
from duyan_util import mysql_util, datetime_util
from duyan_util.kafka_util import KafkaDataConsumer
from duyan_util.mongo_util import BasicDBObject
from jinja2 import Environment, FileSystemLoader
from pymongo import InsertOne, UpdateOne, DeleteMany

from duyan_util import constants
from xhtml2pdf import pisa


def get_pid_by_process_name(process_name):
    """
    通过名称获取进程pid
    :param process_name:
    :return:
    """
    try:
        p_child = subprocess.Popen([f"ps aux | grep {process_name} | grep -v grep | awk '{{print $2}}'"], shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = p_child.communicate()
        return int(bytes.decode(result[0], constants.UTF8))
    except Exception as e:
        return None


def get_local_ipv4_ip():
    """
    获取机器ipv4 ip
    :return:
    """
    interfaces = netifaces.interfaces()
    for inf in interfaces:
        addr = netifaces.ifaddresses(inf)
        ipv4_dict = addr.get(netifaces.AF_INET)
        if ipv4_dict is not None and ipv4_dict[0].get('addr') != '127.0.0.1':
            return ipv4_dict[0].get('addr')


def get_encrypt_phone(phone: str):
    """
    电话号码加密
    :param phone:
    :return:
    """
    if phone is None or len(phone) < 4:
        return phone
    return "*******" + phone[-4:len(phone)]


def get_uuid() -> str:
    """
    uuid生成
    :return:
    """
    return str(uuid.uuid4()).replace("-", "")


def generate_html(template_dir: str, template_name: str, param: dict) -> str:
    """
    html模板渲染
    :param template_dir: 模版文件夹
    :param template_name: 模版名称
    :param param: 参数
    :return:
    """
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    html_content = template.render(param)
    return html_content


def html_to_pdf(html: str) -> bytes:
    """
    html转pdf
    注意:html中需要设置字体 xhtml2pdf 仅支持 STSong-Light
    font-family: STSong-Light
    :param html:
    :return:
    """
    # open output file for writing (truncated binary)
    reader = BytesIO()
    # convert HTML to PDF
    pisa.CreatePDF(html, dest=reader)
    # close output file
    return reader.getvalue()


def get_file_md5(file_path: str):
    try:
        with open(file_path, 'rb') as file_obj:
            digest = md5()
            digest.update(file_obj.read())
            md5_hex = digest.hexdigest()
            return md5_hex
    except Exception as e:
        return "NULL"


def get_file_md5_sub(file_path):
    try:
        child = subprocess.Popen([f"md5sum {file_path}"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        md5val = child.stdout.read()
        return md5val and str(md5val, "utf-8").split(" ")[0] or "NULL"
    except Exception as e:
        return "NULL"


def get_bytes_md5(data: bytes):
    try:
        digest = md5()
        digest.update(data)
        md5_hex = digest.hexdigest()
        return md5_hex
    except Exception as e:
        return "NULL"


def get_communicate_error_result(res):
    if len(res) < 1:
        return None
    if res[1] is not None and res[1] != "" and res[1] != '':
        messge = res[1]
        if isinstance(messge, bytes):
            return str(messge, encoding="utf-8").replace("\n", "")
        else:
            return str(messge).replace("\n", "")
    return None


def is_json(string: str) -> bool:
    """
    判断是否是json字符串
    :param string:
    :return:
    """
    try:
        json.loads(string)
        return True
    except Exception:
        return False


def load_json(json_str: str) -> dict or None:
    """
    json字符串转dict
    :param json_str:
    :return:
    """
    if is_json(json_str):
        if isinstance(json_str, bytes) or isinstance(json_str, bytearray):
            json_str = json_str.decode('utf-8')
        return json.loads(json_str)
    return None


def dump_json(obj) -> str:
    """
    object转json字符串
    :param obj:
    :return:
    """
    return json.dumps(obj, ensure_ascii=False)


class OssUtil:
    OSS_DEFAULT_TIME_OUT = 72 * 60 * 60

    def __init__(self, end_point, access_key_id, access_key_secret, bucket_name):
        """
        Oss文件上次工具类
        :param end_point:
        :param access_key_id:
        :param access_key_secret:
        :param bucket_name:
        """
        self.end_point = end_point
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.bucket_name = bucket_name
        self.bucket = oss2.Bucket(
            oss2.Auth(access_key_id=self.access_key_id, access_key_secret=self.access_key_secret),
            self.end_point, self.bucket_name)

    def upload_to_oss_bytes(self, buffer: bytes, object_name: str, time_out=OSS_DEFAULT_TIME_OUT) -> str:
        """
        上传oss(字节)
        :param time_out: 链接失效时间
        :param buffer: 字节数组
        :param object_name: oss名称
        :return:
        """
        self.bucket.put_object(object_name, buffer)
        oss_url = str(self.bucket.sign_url('GET', object_name, time_out, slash_safe=True))
        return oss_url and oss_url.replace('-internal', '') or None

    def upload_to_oss_by_file_path(self, file_path, object_name, time_out=OSS_DEFAULT_TIME_OUT):
        """
        上传oss(文件)
        :param file_path: 文件路径
        :param object_name: oss名称
        :param time_out: 链接失效时间
        :return:
        """
        self.bucket.put_object_from_file(object_name, file_path)
        oss_url = str(self.bucket.sign_url('GET', object_name, time_out, slash_safe=True))
        return oss_url and oss_url.replace('-internal', '') or None

    def upload_to_oss_by_part(self, file_path, object_name, time_out=OSS_DEFAULT_TIME_OUT):
        """
        分片上传oss(文件)
        :param file_path: 文件路径
        :param object_name: oss名称
        :param time_out: 链接失效时间
        :return: total_size: 文件大小(byte) oss_url: 文件url
        """
        total_size = os.path.getsize(file_path)
        loguru.logger.info(f"..")
        part_size = oss2.determine_part_size(total_size, preferred_size=200 * 1024 * 2014)
        upload_id = self.bucket.init_multipart_upload(object_name).upload_id
        loguru.logger.info(f"开始oss分片上传,文件:{file_path},大小:{total_size}byte,oss分片id:{upload_id}...")
        parts = []
        with open(file_path, 'rb') as file_obj:
            part_number = 1
            offset = 0
            while offset < total_size:
                num_to_upload = min(part_size, total_size - offset)
                # SizedFileAdapter(file_obj, size)方法会生成一个新的文件对象，重新计算起始追加位置。
                result = self.bucket.upload_part(object_name, upload_id, part_number,
                                                 oss2.SizedFileAdapter(file_obj, num_to_upload))
                parts.append(oss2.models.PartInfo(part_number, result.etag))
                offset += num_to_upload
                part_number += 1
                # 完成分片上传。
        self.bucket.complete_multipart_upload(object_name, upload_id, parts)
        oss_url = str(self.bucket.sign_url('GET', object_name, time_out, slash_safe=True))
        oss_url = oss_url and oss_url.replace('-internal', '') or None
        loguru.logger.info(f"oss分片上传上传完成,url:{oss_url}")
        return total_size, oss_url


class Mail(object):
    def __init__(self, smtp_host, smtp_port, host_mail, password):
        """

        :param smtp_host: 邮箱服务host
        :param smtp_port: 邮箱服务port
        :param host_mail: 主邮箱
        :param password: 密码
        """
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.host_mail = host_mail
        self.password = password

    def send_email(self, msg: str, email: list, cc_eamil: list = None, subject: str = None, file_path: str = None,
                   file_name: str = None):
        """

        :param subject: 邮件标题
        :param cc_eamil: 抄送邮箱列表
        :param email: 接收邮箱列表
        :param msg:  邮件正文
        :param file_path:  附件地址
        :param file_name:  附件显示名称
        :return:
        """
        server = None
        try:
            subject = Header(subject or "未命名邮件", 'utf-8')
            send_msg = MIMEText(msg, _subtype='plain', _charset='utf-8')
            me = Header(self.host_mail, 'utf-8')
            m = MIMEMultipart()
            m.attach(send_msg)
            if file_path is not None and os.path.exists(file_path):
                fileApart = MIMEApplication(open(file_path, "rb").read())
                fileApart.add_header("Content-Disposition", "attachment", filename=file_name)
                m.attach(fileApart)
            m['Subject'] = subject
            m['From'] = me
            m['To'] = ";".join(email)
            receiver = email
            if cc_eamil is not None and len(cc_eamil) > 0:
                m['Cc'] = ";".join(cc_eamil)
                receiver.extend(cc_eamil)
            server = smtplib.SMTP_SSL(self.smtp_host, self.smtp_port)
            server.login(self.host_mail, self.password)
            server.sendmail(self.host_mail, receiver, m.as_string())
        except Exception as e:
            raise Exception(e)
        finally:
            if server is not None:
                server.close()


class CMD(object):
    @staticmethod
    @loguru.logger.catch
    def Popen(vars: list):
        child = subprocess.Popen(vars, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        child_result = child.communicate()
        loguru.logger.info(child_result)
        if child_result and len(child_result) > 1:
            message = child_result[1]
            if message is None:
                return
            if isinstance(message, bytes):
                message = str(message, encoding="utf-8")
            if message and len(message) > 0:
                raise Exception(f"执行命令{vars}错误:{message}")


class DataMoveBase(abc.ABC):
    '''
        版本适用 mysql -> mongo 或者 mysql -> mysql
        move_type = 1 为 mysql -> mysql
        move_type = 2 为 mysql -> mongo
        目前其他类型数据搬运不适用

        primary_key_name 是自增主键 类型为 int
    '''
    MYSQL_TO_MYSQL = 1
    MYSQL_TO_MONGO = 2

    CREATE_ACCESS_TABLE = '''
        CREATE TABLE data_access_log ( 
            `id` bigint(20) NOT NULL AUTO_INCREMENT , 
            `platform` int(4) not null default 1 COMMENT '平台类型 ， 1：cti度言 2:anmi安米 ,3: anmi_local 安米本地化 4:sms 短信 ' ,
            `task_sign` varchar(64) not null default '' COMMENT '任务标记' , 
            `batch_uuid` varchar(64) not null default '' COMMENT '批次id ， 系统自动生成 ，每次启动脚本都会变化' ,
            `local_table_name` varchar(64) default '' COMMENT '本地表名' , 
            `target_table_name` varchar(64) default '' COMMENT '目标表名' , 
            `type` int(2) not null default 1 COMMENT '操作类型 ， 1：数据类型搬运日志 ， 2：搬运过程核对日志 ， 3：实时同步核对日志, 4: binlog增量同步' , 
            `status` tinyint(2) not null default 1 COMMENT '结果 ， -1 异常 1 正常' , 
            `access_data` text default null COMMENT '过程日志内容',
            `created_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) COMMENT '数据入库时间' , 
            PRIMARY KEY (`id`),
            key index_created_time(`created_time`) ,
            key index_platform_task_sign( `platform` , `task_sign` )				
	    )
    '''
    INSERT_ACCESS_LOG = ("insert into data_access_log "
                         "(platform ,task_sign , batch_uuid , local_table_name , "
                         "target_table_name , type ,status , access_data )"
                         "value(%s , '%s' ,'%s','%s' , '%s' , %s , %s , '%s')")

    def __init__(self, platform, task_sign, primary_key_name: str, table_name: str, target_table_name: str,
                 local_db, target_db, access_db, is_over_run=False, param_condition=None,
                 move_type: int = 1, default_start_primary_id: int = None,
                 default_last_primary_id=None, scope: int = 999, kafka_consumer: KafkaDataConsumer = None,
                 created_time_field: str = 'created_time', last_updated_time_field: str = 'last_updated_time'):
        '''
            数据同步接口
        :param platform:  平台类型 1：cti度言 2:anmi安米 ,3: anmi_local 安米本地化 4:sms 短信  其他的可以再添加
        :param primary_key_name:  任务的标记 ，用于查询
        :param primary_key_name:  主键名称
        :param table_name:  搬运数据源表名称
        :param target_table_name:  目标表名
        :param param_condition : sql 条件
        :param local_db: 数据源连接
        :param target_db: 目标数据源连接
        :param is_over_run:  是否实时更新
        :param move_type: 适用版本
        :param default_start_primary_id: 默认开始id
        :param scope: 一次性作用数据数量
        :param kafka_consumer: bin_log队列
        :param created_time_field: 创建时间字段名
        :param last_updated_time_field: 最后更新时间字段名
        '''
        self.platform = platform
        if self.platform is None:
            raise Exception("平台类型不能为空")
        self.task_sign = task_sign
        if self.task_sign is None:
            raise Exception("任务标记不能为空")
        self.primary_key_name = primary_key_name
        self.table_name = table_name
        self.target_table_name = target_table_name
        self.move_type = move_type
        self.param_condition = param_condition
        if self.move_type is None or self.move_type not in [self.MYSQL_TO_MYSQL, self.MYSQL_TO_MONGO]:
            raise Exception(f"数据转移类型[{self.move_type}]不是指定类型...")
        self.default_start_primary_id = default_start_primary_id
        self.scope = scope
        self.is_starting = True
        self.start_id = self.default_start_primary_id
        self.local_db = local_db
        self.target_db = target_db
        self.is_over_run = is_over_run
        self.default_last_primary_id = default_last_primary_id
        self.access_db = access_db
        self.batch_uuid = str(uuid.uuid4())
        self.kafka_consumer = kafka_consumer
        self.created_time_field = created_time_field or 'created_time'
        self.last_updated_time_field = last_updated_time_field or 'last_updated_time'

    def load_access_log_db(self, host: str, port: int = None, user_name: str = None, password: str = None,
                           db_name=None):
        '''
            过程日志 数据库连接
        '''
        self.access_db = mysql_util.db(host=host, user=user_name, password=password, port=port, db=db_name,
                                       is_threading=False)

    def save_access_log(self, op_type, access_data, status):
        '''
            过程日志记录
               INSERT_ACCESS_LOG = ("insert into data_access_log "
                         "(platform ,task_sign , batch_uuid , local_table_name , "
                         "target_table_name , type ,status , access_data )"
                         "value(%s , '%s' ,'%s','%s' , '%s' , %s , %s , '%s')")
        '''
        sql = self.INSERT_ACCESS_LOG % (self.platform, self.task_sign, self.batch_uuid, self.table_name,
                                        self.target_table_name, op_type, status, access_data)
        self.access_db.execute(sql)

    def get_start_id(self):
        '''
            从目标库获取 库中第一条数据 作为开始插入数据的第一条(主要用于 断开重启)
        '''
        if self.move_type == self.MYSQL_TO_MYSQL:
            sql = f"select {self.primary_key_name} from {self.target_table_name}  order by {self.primary_key_name} desc limit 1 "
            result = self.target_db.select_one(sql)
            primary_id = result and result.get(self.primary_key_name) or None
            return primary_id and primary_id + 1 or self.default_start_primary_id
        elif self.move_type == self.MYSQL_TO_MONGO:
            result = self.target_db.table.find().sort([(self.primary_key_name, -1)]).limit(1)
            result = result.next()
            return result and result.get(self.primary_key_name) or self.default_start_primary_id
        raise Exception(f"数据转移类型[{self.move_type}]不是指定类型...")

    def get_end_id(self):
        if self.default_last_primary_id:
            return self.default_last_primary_id
        sql = f"select {self.primary_key_name} from {self.table_name} order by {self.primary_key_name} desc limit 1 "
        result = self.local_db.select_one(sql)
        return result and result.get(self.primary_key_name) or 0

    def get_data(self):
        '''
            批量获取数据 可重写
        '''
        if self.is_starting:
            self.is_starting = False
            self.start_id = self.default_start_primary_id if self.default_start_primary_id is not None else self.get_start_id()
        sql = f"select * from {self.table_name} where {self.primary_key_name} between {self.start_id} and {self.start_id + self.scope} {self.param_condition and f'and {self.param_condition}' or ''}"
        return self.local_db.select(sql)

    def full_data_sync(self):
        """
        全量同步
        """
        loguru.logger.info(f"开始同步数据, 从{self.table_name}到{self.target_table_name}")
        while True:
            try:
                target_data_list = self.get_data()
                start_id_tmp = self.start_id
                loguru.logger.info(
                    f"开始同步数据:{self.start_id} - {self.start_id + self.scope} 的数据 共{target_data_list and len(target_data_list) or 0}")
                if target_data_list is None or len(target_data_list) == 0:
                    last_id = self.get_end_id()
                    # 超过了最大值
                    if self.start_id + self.scope > last_id:
                        # 配置继续实时更新的 继续
                        if self.is_over_run:
                            loguru.logger.info("暂无数据，等待实时数据...")
                            time.sleep(5)
                            continue
                        loguru.logger.info("历史数据更新完成...")
                        break
                    self.start_id += self.scope
                    continue

                insert_data = []
                ids = [data.get(self.primary_key_name) for data in target_data_list]
                # 已存在的记录id
                exist_ids = self.__get_target_exists_ids(min(ids), max(ids))
                for data in target_data_list:
                    id_tmp = data.get(self.primary_key_name)
                    if id_tmp > self.start_id:
                        self.start_id = id_tmp
                    # id不存在目标库才插入
                    if id_tmp not in exist_ids:
                        insert_data.append(self.build_data(data))

                self.start_id += 1
                if len(insert_data) > 0:
                    # 是否数据已存在在target表 存在则先删除
                    # self.__check_exist_target_record_and_delete(min(ids), max(ids))
                    # 插入新数据
                    self.insert_data(insert_data, ids)
                self.check_data(start_id_tmp, len(target_data_list), len(insert_data))
            except Exception as e:
                self.save_access_log(1, None, -1)
                loguru.logger.exception(f"数据处理错误:{e}")

    def increment_data_sync(self):
        """
        增量同步kafka bin_log方式 目前只支持数据更新和插入
        """
        if self.kafka_consumer is None or not isinstance(self.kafka_consumer, KafkaDataConsumer):
            raise Exception("数据增量同步需要KafkaConsumer，请您完善配置!")

        loguru.logger.info(f"从kafka获取数据开始....")
        db_logs = self.kafka_consumer.get_data()
        loguru.logger.info(f"从kafka获取数据结束,size:{len(db_logs)}")

        ids = []
        insert_count = 0
        update_count = 0
        delete_count = 0

        insert_list = []
        insert_ids = []
        update_list = []
        update_ids = []
        delete_list = []
        delete_ids = []
        if len(db_logs) > 0:
            for db_log in db_logs:
                if not is_json(db_log):
                    loguru.logger.info(f"消息格式异常:{db_log}")
                db_log_json = load_json(db_log)
                # 数据库名称
                database_name = db_log_json.get("database")
                # 表名
                table_name = db_log_json.get("table")
                # 操作类型
                operation_type = db_log_json.get("type")
                # 不是目标表则跳过
                if database_name != self.local_db.db or table_name != self.table_name:
                    loguru.logger.info(f"消息非{self.table_name},db:{database_name},table:{table_name}")
                    continue
                # 获取数据
                db_records = db_log_json.get("data")

                for db_record in db_records:
                    record_id = int(db_record.get(self.primary_key_name))
                    ids.append(record_id)
                    # 自定义数据处理
                    res = self.increment_data_operation(record_id, operation_type, db_record)
                    if operation_type == "INSERT":
                        insert_list.append(res)
                        insert_ids.append(record_id)
                        insert_count += 1
                    if operation_type == "UPDATE":
                        update_list.append(res)
                        update_ids.append(record_id)
                        update_count += 1
                    if operation_type == "DELETE":
                        delete_list.append(res)
                        delete_ids.append(record_id)
                        update_count += 1
                    # loguru.logger.info(f"同步记录:ID[{record_id}]")

        if len(insert_list) > 0:
            loguru.logger.info(f"新增记录开始,开始id:{min(insert_ids)}, 结束id:{max(insert_ids)}")
            self._do_increment_insert(insert_list)
            loguru.logger.info(f"新增记录结束,开始id:{min(insert_ids)}, 结束id:{max(insert_ids)}")
        if len(update_list) > 0:
            loguru.logger.info(f"更新记录开始,开始id:{min(update_ids)}, 结束id:{max(update_ids)}")
            self._do_increment_update(update_list)
            loguru.logger.info(f"更新记录结束,开始id:{min(update_ids)}, 结束id:{max(update_ids)}")
        if len(delete_list) > 0:
            loguru.logger.info(f"删除记录开始,开始id:{min(delete_ids)}, 结束id:{max(delete_ids)}")
            self._do_increment_delete(delete_list)
            loguru.logger.info(f"删除记录结束,开始id:{min(delete_ids)}, 结束id:{max(delete_ids)}")

        if len(ids) > 0:
            # 校验日志
            access_log_data = {
                "id": {
                    "s": min(ids),
                    "e": max(ids)
                },
                "binlog_size": len(ids),
                "insert_size": insert_count,
                "update_size": update_count,
                "delete_size": delete_count
            }
            loguru.logger.info(access_log_data)
            # self.save_access_log(4, json.dumps(access_log_data), 1)

    def check_data(self, start_id, query_size, insert_size):
        """
        按批次检查
        """
        if self.move_type is None or self.move_type not in [self.MYSQL_TO_MYSQL, self.MYSQL_TO_MONGO]:
            raise Exception(f"数据转移类型[{self.move_type}]不是指定类型...")
        loguru.logger.info(f"数据核对开始,start_id:{start_id},end_id:{start_id + self.scope}")
        # 原表数据数量
        local_count = self.__get_local_data_count(start_id)
        # 目标表数据数量
        target_count = self.__get_target_data_count(start_id)
        # 数据核对 遗漏数据补齐
        missing_data_list = []
        missing_ids = []
        if local_count > target_count:
            # 原表数据
            data_list = self.__get_local_data(start_id)
            # 目标表数据
            target_data_list = self.__get_target_data(start_id)
            # 比对得到漏掉多数据
            target_id_list = [target_data.get(self.primary_key_name) for target_data in target_data_list]
            for _data in data_list:
                local_id = _data.get(self.primary_key_name)
                if local_id not in target_id_list:
                    missing_data = self.build_data(_data)
                    missing_data_list.append(missing_data)
                    missing_ids.append(local_id)
                    loguru.logger.info(f"missing record:{missing_data}")

        # 遗漏数据补齐
        if len(missing_data_list) > 0:
            self.insert_data(missing_data_list, missing_ids)
            loguru.logger.info(f"数据补齐条数:{len(missing_data_list)},start_id:{start_id},end_id:{start_id + self.scope}")
        loguru.logger.info(f"数据核对结束,start_id:{start_id},end_id:{start_id + self.scope}")

        # 校验日志
        access_log_data = {
            "id": {
                "s": start_id,
                "e": self.start_id
            },
            "size": query_size,
            "insert_size": insert_size,
            "check": {
                "local": local_count,
                "target": target_count
            }
        }
        self.save_access_log(2, json.dumps(access_log_data), local_count == target_count and 1 or -1)

    def check_data_daily(self, check_day: date = None, minute: int = 5):
        """
        按天检查 默认每批次比对1000条 默认为前一天
        :param check_day: 核对日期 默认不填为前一天
        :param minute: 时间分段核对间隔 默认5分钟 循环每次查5分钟数据进行比对 最小1分钟
        :return:
        """
        # TODO 优化：1 . 按指定时间间隔分割循环核对 2. 可传核对的count字段列表 都count一下，不同就比对
        if check_day is None:
            check_day = date.today() - timedelta(days=1)
        try:
            # 统计总数
            local_count_total = 0
            target_count_total = 0

            # 开始结束时间 时间间隔
            start_date_time = datetime(year=check_day.year, month=check_day.month, day=check_day.day, hour=0, minute=0,
                                       second=0)
            end_date_time = datetime(year=check_day.year, month=check_day.month, day=check_day.day, hour=23, minute=59,
                                     second=59)
            # 最小跨度5 分钟
            grep_minute = 5 if not minute or minute < 5 else minute

            # 本段开始结束时间
            round_start = start_date_time
            round_end = start_date_time + timedelta(minutes=grep_minute - 1, seconds=59)
            round_end = end_date_time if round_end > end_date_time else round_end
            # 按时间grep_minute拆分分页比对
            miss_data_list = list()
            while round_end <= end_date_time:
                start = round_start.strftime(datetime_util.DEFAULT_DATETIME_FORMAT)
                end = round_end.strftime(datetime_util.DEFAULT_DATETIME_FORMAT)
                loguru.logger.info(f"日期:{check_day},数据核对开始,核对时间:{start}-{end}")

                # 原表数据数量
                local_count = self.__get_local_data_count_daily(start, end) or 0  # 默认 0
                local_count_total += local_count
                # 目标表数据数量
                target_count = self.__get_target_data_count_daily(start, end) or 0
                target_count_total += target_count
                loguru.logger.info(f"日期:{check_day},local_count:{local_count},target_count:{target_count} , "
                                   f"数据{local_count == target_count and '一致。' or '不一致！'}")

                # 数据批量核对 用不等于
                # 用于记录缺失的数据

                if not local_count == target_count:
                    # loguru.logger.info(f"日期:{check_day},数据核对存在不一致，开始处理")
                    # 缺失的数据
                    missing_records = []
                    missing_records_ids = []
                    # 分页参数
                    start_row = 0
                    # 今日原表数据
                    local_data_list = self.__get_local_data_batch_by_day(start, end, start_row)
                    while len(local_data_list) > 0:
                        for local_data in local_data_list:
                            data_id = local_data.get(self.primary_key_name)
                            # 查询
                            target_date = self.__get_target_data_by_primary_key(data_id)
                            # 校验是否存在，不存在加入missing_records列表等待重新插入
                            if target_date is None:
                                miss_data_list.append(data_id)
                                missing_data = self.build_data(local_data)
                                missing_records.append(missing_data)
                                missing_records_ids.append(data_id)
                                loguru.logger.info(f"日期:{check_day},missing record:{missing_data}")
                        # 下一批数据
                        start_row += self.scope
                        local_data_list = self.__get_local_data_batch_by_day(start, end, start_row)

                    if len(missing_records) > 0:
                        loguru.logger.info(f"日期:{check_day},{start}-{end},遗漏数据开始导入...")
                        self.insert_data(missing_records, missing_records_ids)
                        loguru.logger.info(f"日期:{check_day},{start}-{end},遗漏数据开始导入结束...")

                # else:
                #     loguru.logger.info(f"日期:{check_day},{start}-{end},数据一致，无需处理")
                # 计算下一段时间
                round_start = round_end + timedelta(seconds=1)  # (round_end + timedelta(minutes=1)).replace(second=0)
                round_end = round_start + timedelta(minutes=grep_minute - 1, seconds=59)

            loguru.logger.info(f"日期:{check_day},数据核对结束...")
            # 校验日志
            access_log_data = {
                "start_time": start_date_time.strftime(datetime_util.DEFAULT_DATETIME_FORMAT),
                "end_time": end_date_time.strftime(datetime_util.DEFAULT_DATETIME_FORMAT),
                "check": {
                    "local": local_count_total,
                    "target": target_count_total,
                    "miss": miss_data_list
                }
            }
            self.save_access_log(3, json.dumps(access_log_data), 1)
        except Exception as e:
            message = f"数据处理错误:{e}"
            self.save_access_log(1, json.dumps({'error': message}), -1)
            loguru.logger.exception(f"数据处理错误:{e}")

    def __get_local_data(self, start_id):
        local_select_sql = f"select * from {self.table_name} where {self.primary_key_name} between {start_id} and {start_id + self.scope}"
        data_list = self.local_db.select(local_select_sql)
        return data_list

    def __get_target_data_count(self, start_id):
        if self.MYSQL_TO_MYSQL == self.move_type:
            return self.__get_target_data_count_mysql(start_id)
        elif self.MYSQL_TO_MONGO == self.move_type:
            return self.__get_target_data_count_mongo(start_id)

    def __get_target_data(self, start_id):
        if self.MYSQL_TO_MYSQL == self.move_type:
            return self.__get_target_data_mysql(start_id)
        elif self.MYSQL_TO_MONGO == self.move_type:
            return self.__get_target_data_mongo(start_id)

    def __get_target_data_mongo(self, start_id):
        target_select_sql = BasicDBObject()  # {self.primary_key_name : {"$gte" : start_id , "$lte" : }}
        target_select_sql.between(self.primary_key_name, start_id, start_id + self.scope)
        target_data_list = self.target_db.table.find(target_select_sql)
        return target_data_list

    def __get_target_data_mysql(self, start_id):
        target_select_sql = f"select * from {self.target_table_name} where {self.primary_key_name} between {start_id} and {start_id + self.scope}"
        target_data_list = self.target_db.select(target_select_sql)
        return target_data_list

    def __get_target_data_count_mongo(self, start_id):
        target_count_sql = BasicDBObject()  # {self.primary_key_name : {"$gte" : start_id , "$lte" : }}
        target_count_sql.between(self.primary_key_name, start_id, start_id + self.scope)
        target_count = int(self.target_db.table.count_documents(target_count_sql) or 0)
        return target_count

    def __get_local_data_count(self, start_id):
        local_count_sql = f"select count(1) as c from {self.table_name} where {self.primary_key_name} between {start_id} and {start_id + self.scope}"
        local_count_obj = self.local_db.select_one(local_count_sql)
        local_count = int(local_count_obj and local_count_obj.get("c") or 0)
        return local_count

    def __get_target_data_count_mysql(self, start_id):
        target_count_sql = f"select count(1) as c from {self.target_table_name} where {self.primary_key_name} between {start_id} and {start_id + self.scope}"
        target_count_obj = self.target_db.select_one(target_count_sql)
        target_count = int(target_count_obj and target_count_obj.get("c") or 0)
        return target_count

    def __get_local_data_batch_by_day(self, day_start, day_end, start_row):
        local_select_sql = f"select * from {self.table_name} where {self.created_time_field} between '{day_start}.000' and '{day_end}.999' limit {start_row}, {self.scope}"
        data_list = self.local_db.select(local_select_sql)
        return data_list

    def __get_target_data_by_primary_key(self, data_id):
        if self.MYSQL_TO_MYSQL == self.move_type:
            return self.target_db.select_one(
                f"select * from {self.target_table_name} where {self.primary_key_name} = {data_id}")
        elif self.MYSQL_TO_MONGO == self.move_type:
            target_count_sql = BasicDBObject().eq(self.primary_key_name, data_id)
            return self.target_db.table.find_one(target_count_sql)

    def __get_local_data_count_daily(self, day_start, day_end):
        local_count_sql = f"select count(1) as c from {self.table_name} where {self.created_time_field} between '{day_start}.000' and '{day_end}.999'"
        local_count_obj = self.local_db.select_one(local_count_sql)
        local_count = int(local_count_obj and local_count_obj.get("c") or 0)
        return local_count

    def __get_target_data_count_daily(self, day_start, day_end):
        """
        target库记录按日统计
        """
        if self.MYSQL_TO_MYSQL == self.move_type:
            return self.__get_target_data_count_daily_mysql(day_start, day_end)
        elif self.MYSQL_TO_MONGO == self.move_type:
            return self.__get_target_data_count_daily_mongo(day_start, day_end)

    def __get_target_data_count_daily_mysql(self, day_start, day_end):
        """
        target库记录按日统计 mysql
        """
        target_count_sql = f"select count(1) as c from {self.target_table_name} where {self.created_time_field} between '{day_start}.000' and '{day_end}.999'"
        target_count_obj = self.target_db.select_one(target_count_sql)
        target_count = int(target_count_obj and target_count_obj.get("c") or 0)
        return target_count

    def __get_target_data_count_daily_mongo(self, day_start, day_end):
        """
        target库记录按日统计 mongo
        """
        target_count_sql = BasicDBObject()
        target_count_sql.between(self.created_time_field, day_start, day_end)
        target_count = int(self.target_db.table.count_documents(target_count_sql) or 0)
        return target_count

    def __check_exist_target_record_and_delete(self, min_data_id, max_data_id):
        """
        检查并删除已存在的记录
        """
        # mysql先删除再插入
        if self.MYSQL_TO_MYSQL == self.move_type:
            if self.__count_exist_target_record_mysql(min_data_id, max_data_id) > 0:
                sql = f"delete from {self.target_table_name} where {self.primary_key_name} between {min_data_id} and {max_data_id}"
                self.target_db.execute(sql)
        elif self.MYSQL_TO_MONGO == self.move_type:
            # if self.__count_exist_target_record_mongo(min_data_id, max_data_id) > 0:
            #     sql = BasicDBObject()
            #     sql.between(self.primary_key_name, min_data_id, max_data_id)
            #     self.target_db.table.remove(sql)
            pass

    def __count_exist_target_record_mysql(self, min_data_id, max_data_id):
        """
        按主键范围统计target库记录 mysql
        """
        sql = f"select count(1) as `count` from {self.target_table_name} where {self.primary_key_name} between {min_data_id} and {max_data_id}"
        rs = self.target_db.select_one(sql)
        return rs.get('count') or 0

    def __count_exist_target_record_mongo(self, min_data_id, max_data_id):
        """
        按主键范围统计target库记录 mongo
        """
        sql = BasicDBObject()
        sql.between(self.primary_key_name, min_data_id, max_data_id)
        target_count = int(self.target_db.table.count_documents(sql) or 0)
        return target_count

    def __get_target_exists_ids(self, start_id, end_id):
        if self.MYSQL_TO_MYSQL == self.move_type:
            records = self.target_db.select(
                f"select {self.primary_key_name} from {self.target_table_name} where {self.primary_key_name} between {start_id} and {end_id}")
            return [record.get(self.primary_key_name) for record in records]
        elif self.MYSQL_TO_MONGO == self.move_type:
            sql = BasicDBObject()
            sql.between(self.primary_key_name, start_id, end_id)
            cursor = self.target_db.table.find(sql, {self.primary_key_name: True})
            return [record.get(self.primary_key_name) for record in cursor]

    def _do_increment_insert(self, insert_list):
        insert_one_list = [InsertOne(one) for one in insert_list]
        self.target_db.table.bulk_write(insert_one_list)

    def _do_increment_update(self, update_list):
        replace_one_list = [
            UpdateOne(filter={self.primary_key_name: one.get(self.primary_key_name)}, update={'$set': one}, upsert=True)
            for one in update_list]
        self.target_db.table.bulk_write(replace_one_list)

    def _do_increment_delete(self, delete_list):
        delete_ids = [one.get(self.primary_key_name) for one in delete_list]
        self.target_db.table.bulk_write([DeleteMany(filter={self.primary_key_name: {'$in': delete_ids}})])

    @abc.abstractmethod
    def insert_data(self, insert_values: list, insert_parmary_ids: list):
        '''
            数据插入
        :param insert_values:  插入的数据列表
        :param insert_parmary_ids:  插入的id列表 ， 可以用这个去删除重复数据
        :return:
        '''
        ...

    @abc.abstractmethod
    def build_data(self, data):
        '''
            数据处理 需要继承实现
        :param data:
        :return:
        '''
        ...

    @abc.abstractmethod
    def increment_data_operation(self, primary_key_value, bin_log_type, bin_log_record):
        """
        增量同步处理binlog数据
        """
        ...


if __name__ == '__main__':
    # CMD.Popen(["tail -n 100 /Users/wangchunyang/Desktop/hosts "])
    # loguru.logger.info(str(uuid.uuid4()))
    print(
        f'''{{"id" :{{"s" : 1 , "e" : 1 }} , "size" : 1 , "insert_size" :1 ,"check" : {{ "local" : 1 , "target" : 1 }} }} ''')
