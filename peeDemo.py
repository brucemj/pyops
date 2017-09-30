# -*- coding: UTF-8 -*-

# http://docs.peewee-orm.com/en/latest/index.html
from peewee import *
import time, datetime
#import userservicetest as dbsrc
#import userservicebak as dbdst
import cssover as dbsrc
import cssoverbak as dbdst
import log as logmj

logfile = 'baksql.log'
log = logmj.console_set(logfile, lvl=2)

# db_dst = MySQLDatabase('userservicebak', **{'host': '172.21.12.120', 'password': 'tmp', 'user': 'tmp', 'charset':'utf8'})
# CREATE DATABASE IF NOT EXISTS userservicebak DEFAULT CHARSET utf8 COLLATE utf8_general_ci ;
# mysqldump -h localhost -uroot -p123456  -d database > dump.sql
# userservicetest.sql

# http://docs.peewee-orm.com/en/latest/peewee/querying.html#creating-a-new-record
# elecimage = dbsrc.Elecimage.select().join(dbsrc.Elecimage)

def time_txt():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
def time_ms():
    return  time.time()

def find_max_id(dbname, tbname, tbkey):
    # args : dbname, tbname, tbkey , all are string
    # 字符串作为变量名 vars eval
    # http://blog.csdn.net/ztf312/article/details/51122027
    # return max_id = 0 ; if max_id is None

    tb_fname = '.'.join([dbname, tbname])
    tb_fkey = '.'.join([dbname, tbname, tbkey])
    select_max = eval(tb_fname).select(
        fn.Max(eval(tb_fkey))
    )

    max_id = select_max[0]._data[tbkey]
    max_id = max_id if not (max_id is None) else 0
    return max_id


def select_data_by_id(dbname, tbname, tbkey, max_id=0, rownum=10):
    # args : dbname, tbname, tbkey, max_id, rownum=10
    # 字符串作为变量名 vars eval

    tb_fname = '.'.join([dbname, tbname])
    tb_fkey = '.'.join([dbname, tbname, tbkey])
    select_data = eval(tb_fname).select().where(
        eval(tb_fkey) > max_id
    ).limit(rownum)
    return select_data


def insert_data(dbname, tbname, dataiter):
    # data_source = [
    #     {'student_name': 'hom', 'student_no': 888},
    #     {'student_name': 'baby', 'student_no': 889}
    # ]
    # # 方法2（这个方法会快很多）
    # with database.atomic():
    #     for data_dict in data_source:
    #         StudentsInfo.create(**data_dict)
    # # 方法3（最快的方法）
    # with database.atomic():
    #     for idx in range(0,len(data_source),100):
    #     StudentsInfo.insert_many(data_source[idx:idx+100]).execute()
    tb_fname = '.'.join([dbname, tbname])
    insert_step = 5000
    datalen = dataiter.__len__()
    with eval(dbname).database.atomic():
        n, data = 0, []
        def exeinsert(tb_fname, data):
            eval(tb_fname).insert_many(data).execute()
            log.info( '      ...   %s %s insert_data finish' % (tb_fname, n) )

        for o in dataiter:
            n += 1
            data.append(o._data)
            if n % insert_step == 0 :
                exeinsert(tb_fname, data)
                data = []
        if not (data == []):
            exeinsert(tb_fname, data)
            data = []

if __name__ == "__main__":
    tables_neixiao = [
        {'name': 'Appinfo', 'numkey': 'appinfo'},
        {'name': 'Appinstall', 'numkey': 'installid'},
        {'name': 'Baseinfo', 'numkey': 'baseinfo'},
        {'name': 'Chargeinfo', 'numkey': 'id'},
        {'name': 'Elecimage', 'numkey': 'i'},
        {'name': 'Electroniccard', 'numkey': 'card'},
        {'name': 'Feedbackprocess', 'numkey': 'processid'},
        {'name': 'Imeinetwork', 'numkey': 'card'},
        {'name': 'Locationinfo', 'numkey': 'location'},
        {'name': 'Loginfo', 'numkey': 'logid'},
        {'name': 'Repairrecord', 'numkey': 'r'},
        {'name': 'Softwareversion', 'numkey': 'softversion'},
        {'name': 'Userfeedback', 'numkey': 'userfeedback'},
        {'name': 'Warrantydate', 'numkey': 'wid'}
        # Nation - -------------------
        # SysDictionary - -------------------
        # SysDictionarytype - -------------------
        # SysOrganization - -------------------
        # SysResource - -------------------
        # SysRole - -------------------
        # SysRoleResource - -------------------
        # SysUser - -------------------
        # SysUserRole - -------------------
        # Website - -------------------
    ]
    tables = [
        {'name': 'Appinfo', 'numkey': 'appinfo'},
        {'name': 'Appinstall', 'numkey': 'installid'},
        {'name': 'Baseinfo', 'numkey': 'baseinfo'},
        {'name': 'Chargeinfo', 'numkey': 'id'},
        {'name': 'Country', 'numkey': 'countryid'},
        {'name': 'Elecimage', 'numkey': 'i'},
        {'name': 'Elecimageover', 'numkey': 'i'},
        {'name': 'Electroniccard', 'numkey': 'card'},
        {'name': 'Electroniccardover', 'numkey': 'overid'},
        # {'name': 'Feedbackprocess', 'numkey': 'processid'},
        # {'name': 'Imeinetwork', 'numkey': 'card'},
        # {'name': 'Locationinfo', 'numkey': 'location'},
        {'name': 'Loginfo', 'numkey': 'logid'},
        {'name': 'OdmOwn', 'numkey': 'ooid'},
        {'name': 'Odmcard', 'numkey': 'odmid'},
        {'name': 'OdmcardCopy', 'numkey': 'odmid'},
        {'name': 'Repairrecord', 'numkey': 'r'},
        {'name': 'Servicephone', 'numkey': 'phoneid'},
        {'name': 'Softwareversion', 'numkey': 'softversion'},
        {'name': 'Userfeedback', 'numkey': 'userfeedback'},
        {'name': 'Warrantydate', 'numkey': 'wid'},
        {'name': 'Website', 'numkey': 'w'},
        {'name': 'Websiteover', 'numkey': 'w'},

        # Nation - -------------------
        # SysDictionary - -------------------
        # SysDictionarytype - -------------------
        # SysOrganization - -------------------
        # SysResource - -------------------
        # SysRole - -------------------
        # SysRoleResource - -------------------
        # SysUser - -------------------
        # SysUserRole - -------------------
        # Website - -------------------
        # Mcccode -------------------
    ]

    # http://blog.csdn.net/huangxiongbiao/article/details/49535803  异常处理和性能的影响
    while True:
        try:
            for t in tables:
                tbname , tbkey = t['name'] , t['numkey']
                datanum = 1000000
                src_max_id = find_max_id('dbsrc', tbname, tbkey)
                dst_max_id = find_max_id('dbdst', tbname, tbkey)

                if dst_max_id < src_max_id :
                    log.info('%s max_id= %s/%s ; %s will be insert.' % (tbname, dst_max_id, src_max_id, datanum))
                    select_data = select_data_by_id('dbsrc', tbname, tbkey, max_id=dst_max_id, rownum=datanum)
                    insert_data('dbdst', tbname, select_data)
                else:
                    #log.info('%s max_id= %s/%s ; no update.' % (tbname, dst_max_id, src_max_id))
                    pass
        except Exception, e:
            #log.error(e)
            pass

        time.sleep(3)

