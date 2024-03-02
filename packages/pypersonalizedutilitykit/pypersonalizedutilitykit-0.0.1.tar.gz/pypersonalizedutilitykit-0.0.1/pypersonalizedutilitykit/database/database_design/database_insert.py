# -*- coding:utf-8 -*-
"""
# File       : database_insert.py
# Time       ：2023/1/21
# Author     ：lyz
# version    ：python 3
# Description：
"""
import datetime
import gc

from faker import Faker

from yiXie_2_util.database.database_design.database_base import DbOperation
'''
sql语句   根据实际情况修改语句
'''
sql = "insert into mysql_test_database_2023_1_18.test1(_random_int,_address,_ssn,_company,_credit_card_full,_name,_phone_number," \
      "_ascii_company_email,_domain_name,_chrome,_text,_password,_date_object,_profile) values(%s,%s,%s,%s,%s,%s" \
      ",%s,%s,%s,%s,%s,%s,%s,%s)"
f = Faker(locale='zh_CN')
# "insert into table1(_varchar,_number,_float,_time,_DECIMAL) values(%s,%s,%s,%s,%s)"
def func_insert(class_feature,sql,flag=0):
    '''
    插入函数
    :param class_featuree:实例化数据库类
    :param flag:记录次数
    :param sql:插入语句
    '''
    startTime = datetime.datetime.now()
    for i in range(1000000):  # 1.设置插入次数
        data_list_all = []  # 存储所有字段值
        startTime1 = datetime.datetime.now()    # 每一次插入用时 起始
        for n in range(10):  # 2.批量插入数量
            data_list = []  # 存储字段值
            data_list.extend((int(f.int()),f.address(),f.ssn(),f.company(),f.credit_card_full()
                ,f.name(),int(f.phone_number()),f.ascii_company_email(),f.domain_name()
                ,f.chrome(),f.text(),f.password(),f.date_object(),str(f.profile())))   # 添加字段值
            data_list_all.append(data_list) # 添加所有字段值
            flag = flag + 1 # 总数
        else:
            # 3.插入语句
            # class_feature.insert_data("insert into table1(_varchar,_number,_float,_time,_DECIMAL) values(%s,%s,%s,%s,%s)",
            #                data_list_all)
            class_feature.insert_data(sql,data_list_all)
            print("总数量：{}".format(flag))
            del data_list   # 删除变量
            gc.collect()    # 回收空间
            endTime1 = datetime.datetime.now()  # 每一次插入用时 结束
        print('第{}轮新增完毕，耗时：'.format(i + 1), endTime1 - startTime1)
        endTime = datetime.datetime.now()
        print('已耗时:', endTime - startTime, '\n')
        # if do.select_data("select _bigint from table5 where _bigint = {}".format(num3)):
        #     print("数量：{}".format(flag))
        #     flag = flag + 1
        # print("数量：{}".format(flag))
        del data_list_all   # 删除变量
        gc.collect()    # 回收空间
    else:
        print('新增完毕')
    endTime = datetime.datetime.now()   # 设置结束插入时间
    print('总耗时:', endTime - startTime)


if __name__ == '__main__':
    do = DbOperation('localhost','mysql_test_database_2023_1_18')
    func_insert(do,sql)