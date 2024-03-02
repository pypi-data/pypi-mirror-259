# -*- coding:utf-8 -*-
"""
# File       : database_table.py
# Time       ：2023/1/18 
# Author     ：lyz
# version    ：python 3
# Description：
"""
from yiXie_2_util.database import DbOperation

def func_database(host_p,sql):
    '''
    创建库
    :param host_p: IP地址 localhost
    :param sql: 语句  CREATE database test
    :return:
    '''
    return DbOperation(host_p).create_database(sql)

def func_datatable(host_p,sql):
    '''
    创建表
    :param host_p: IP地址 localhost
    :param sql: 语句  CREATE TABLE test.test1(_num int)
    :return:
    '''
    return DbOperation(host_p).create_table(sql)

if __name__ == '__main__':
    # func_database('localhost', 'CREATE database 2023_1_18')
    sql = "CREATE TABLE mysql_test_database_2023_1_18.test1(_random_int int,_address varchar(255),_ssn varchar(255),_company varchar(255)," \
          "_credit_card_full text,_name char(255),_phone_number int,_ascii_company_email char(255),_domain_name char(255),_chrome char(255)," \
          "_text varchar(255),_password char(255),_date_object time,_profile text)"
    # sql = "CREATE TABLE 2023_1_18.test1(" \
    #                "_num int)"

    # print(sql)
    func_datatable('localhost', sql)