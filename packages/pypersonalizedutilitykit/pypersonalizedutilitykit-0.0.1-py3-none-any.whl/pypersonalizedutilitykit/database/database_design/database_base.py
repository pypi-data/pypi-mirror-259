# -*- coding:utf-8 -*-
"""
# File       : database_base.py
# Time       ：2023/1/18 
# Author     ：lyz
# version    ：python 3
# Description：
"""
import re
import time

import pymysql
from hamcrest import assert_that, equal_to
from yiXie_1_config.baseConfig import *
from yiXie_2_util.base_tool import responseJudgment, covertStr
from yiXie_2_util.log import Error, Info
class DbOperation:
    def __init__(self, user_n, password_s, port_n, host_p, database_n=None):
        # 创建连接(管道)
        self.db = database_n
        try:
            self.conn = pymysql.Connection(host=host_p, user=user_n, password=password_s,
                                           database=database_n, port=port_n, charset='utf8')
            Info.log(f'{self.conn}connect success!')
        except Exception as error:
            raise Error.log(f"connect failed: {error}")
    # CREATE database test
    def create_database(self, sql_s):
        '''
        创建数据库
        :param sql_s: 语句
        :return:
        '''
        try:
            # 创建游标(字典方式展示)
            self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            # sql_createTb =
            '''
            CREATE database test
            '''
            self.cur.execute(sql_s)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            print('创建库成功!' + sql_s)

    # CREATE TABLE test.test1(_num int)
    def create_table(self, sql_s):
        '''
        创建表
        :param sql_s: 语句
        :return:
        '''
        try:
            # 创建游标(字典方式展示)
            self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            # sql_createTb =
            '''
            sql_createTb = "
             CREATE TABLE test.test1(_num int) "
            '''
            self.cur.execute(sql_s)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            print('创建表成功!' + sql_s)

    # so.insert_data("insert into customer_info(customer_id) values(50)")
    def insert_data(self, sql_s, data_list):
        '''
        插入数据
        :param sql_s: 语句
        :param data_list: 存储语句的列表
        :return:
        '''
        try:
            # 自动重连
            # self.conn.ping(True)
            # 创建游标(字典方式展示)
            self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            # 执行SQL
            total_count = self.cur.executemany(sql_s, data_list)  # 批量添加
            self.conn.commit()  # 提交数据
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            print('insert success!' + sql_s)
            print('新增：', total_count)
        # finally:
        #     # 关闭游标
        #     self.cur.close()
        #     # 关闭连接
        #     self.conn.close()

    # so.delete_data("delete from customer_info where customer_id = 50")
    def delete_data(self, sql_s):
        try:
            # 创建游标(字典方式展示)
            self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            # 执行SQL
            self.cur.execute(sql_s)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            Info.log('delete success!' + sql_s)
        # finally:
        #     # 关闭游标
        #     self.cur.close()
        #     # 关闭连接
        #     self.conn.close()

    # so.update_data("update customer_info set user_id = 5 where user_id = 7 ")
    def update_data(self,sql_s):
        try:
            # 创建游标(字典方式展示)
            self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            # 执行SQL
            self.cur.execute(sql_s)
            self.conn.commit()                  #提交数据
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            print('update success!' + sql_s)
        # finally:
        #     # 关闭游标
        #     self.cur.close()
        #     # 关闭连接
        #     self.conn.close()

    # so.search_data("select * from customer_info where customer_id = 50 ")
    def select_data(self,sql_s):
        try:
            # 创建游标(字典方式展示)
            self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            # 执行SQL
            self.cur.execute(sql_s)
            # 通过游标的fetchall方法，获取数据                 查找独有
            res = self.cur.fetchall()
            # 打印数据
            print(res)
        except Exception as e:
            print(e)
            self.conn.rollback()
        # finally:
        #     # 关闭游标
        #     self.cur.close()
        #     # 关闭连接
        #     self.conn.close()
        return res

    def single_table_select_sql(self, column_name, your_table, *args):
        """
        单表查询
        Args:
            column_name: 需要查询的字段名
            your_table: 需要查询的表名
        Returns: 查询结果
        """
        query = ''  # 初始化 query 变量
        # 查询where 判断
        if isinstance(column_name, (list, tuple)):
            query = f"SELECT {','.join(column_name)} FROM {your_table} WHERE "
        elif isinstance(column_name, str):
            query = f"SELECT {column_name} FROM {your_table} WHERE "
        else:
            Error.log(f"An typeError occurred: {column_name}")
            print("[请输入 list/tuple/str 类型数据!]")
        # 获取数据
        for condition in args:
            # 除开where以外的语句
            if "ORDER BY" in str(condition).upper() or "GROUP BY" in str(condition).upper() or "LIMIT" in str(condition).upper():  # ORDER BY、GROUP BY
                if "NONE" not in str(condition).upper():
                    query = query[:-4]  # 移除无条件的and
                    query += f"{condition} "
                    query += 'AND '
            else:
                field, operator, value, condit = condition
                if "NONE" in condit.upper():  # condit 判断，为空，则补上AND
                    condit = 'AND'
                if "AND" not in condit.upper() and "OR" not in condit.upper():    # condit 判断，既没有AND也没有OR，补上AND。
                    condit += ' AND'                                              # 例：condit 上有个括号 (
                # 剔除传入的null值，排除 between,in 条件。原因：between 和 in 值不能加引号，否则报错!
                if "NONE" not in str(value).upper() and "BETWEEN" not in str(operator).upper() and "IN" not in str(operator).upper():
                    query += f'{field} {operator} \'{value}\' {condit} '
                # 剔除传入的null值，使用between。原因：between 传入两个值，进行特殊处理
                if "NONE" not in str(value).upper() and "BETWEEN" in str(operator).upper():
                    between = re.findall("between", str(operator))
                    between_value = re.search(r'(?<=between)+.*', str(operator))
                    andd = re.findall("and", str(value))
                    and_value = re.search(r'(?<=and)+.*', str(value))
                    query += f'{field} {between[0]} \'{between_value[0]}\' {andd[0]} \'{and_value[0]}\' {condit} '
                # 剔除传入的null值，使用in
                if "NONE" not in str(value).upper() and "IN" in str(operator).upper():
                    query += f'{field} {operator} {value} {condit} '
        if "AND" not in query.upper() and "OR" not in query.upper():    # 当所有条件值都为空时，返回None
            query += f'0 = 1 AND '
        if query:
            query = query[:-4]  # 移除无条件的and
            # query += 'is_delete = 1 ORDER BY create_time DESC'
            # query += 'ORDER BY create_time DESC'
        Info.log(query)     # 日志记录sql语句
        return query

    def assert_datatable(self, your_table, column_name, expect_db=None, *args):
        '''
        数据表断言   （一般用在增/改时，用刚增/改的元素与数据库中值进行对比，能对比上说明入库成功）
        :param your_table: 表名
        :param column_name: 列名  1、列表["id", "ces"]   2、元组("id", "ces")   3、字符串"user_base_id"
        :param expect_db: 期望值  1、元组 (892458041165238272,1)     2、字符串 "name"     3、整形 123
        :param *args: 语句 where 数据值  ("user_base_id", "=", "892458041165238272"),("id", "like", "72%")
        :return:
        assert_database("tb_recharge_record", ["user_base_id", "is_succes"], (892458041165238272,1),
                       ("user_base_id", "=", "892458041165238272"),("is_succes", "=", 1))
        '''
        try:
            self.cur = self.conn.cursor(cursor=pymysql.cursors.Cursor)  # 创建游标(默认方式展示)
            sql = self.single_table_select_sql(column_name, your_table, *args)  # 返回 sql 语句
            self.cur.execute(sql)   # 执行
            # 通过游标的fetchall方法，获取数据  查找独有          含有DISTINCT则只取第一个字段值。其他情况则取所有
            actual = [[m[0] for m in self.cur.fetchall() if m[0]]] if "DISTINCT" in sql.upper() else self.cur.fetchall()
            # 断言(actual为字典方式获取值!)
            if actual is ():    # 查询结果为空
                if expect_db is not None:
                    assert_that('None', equal_to(expect_db),
                                reason=f"[Table assertion failed: 表[{your_table}] → 字段[{column_name}] 期望值 {expect_db} 与 查询值 'None' 不等，请检查!")
                    Info.log(f"Table assertion success: 表[{your_table}] → 字段[{column_name}] 期望值 等于 查询值，测试结束!\n")
                else:
                    return None
            else:
                # 将所有数值型转换为字符串(注意：这里指的是字段的值是普通格式，即非列表、非字典、非枚举、非元组、非集合等类型)
                actual = covertStr(actual)
                if expect_db is not None:    # 期望值非空
                    if len(actual[0]) > 1:   # 字段2列及以上。
                        arg = [row for row in actual]                       # 2行及以上数据时，返回所有数据 arg
                        actual = arg if len(arg) > 1 else actual[0]        # 只有1行数据，则返回第1行数据 actual[0]
                    elif len(actual[0]) == 1:  # 字段只有1列。
                        arg = [row[0] for row in actual]    # 2行及以上数据时，返回所有数据 arg 。目的：多行数据 与 接口返回的数据进行JSONpath操作后进行比较。
                        actual = arg if len(arg) > 1 else actual[0][0]     # 只有1行数据，则返回第1行数据 actual[0][0]
                    if isinstance(actual, (list, tuple, dict, set)) and isinstance(expect_db,(list, tuple, dict, set)):
                        actual = sorted(actual)      # 列表、元组、字典、集合
                        expect_db = sorted(expect_db)  # 排序
                    # if isinstance(expect_db, str) and expect_db.isdigit():
                    #     expect_db = int(expect_db)
                    assert_that(actual, equal_to(expect_db),
                                reason=f"[Table assertion failed: 表[{your_table}] → 字段[{column_name}] 期望值 {expect_db} 与 查询值 {actual} 不等，请检查!")
                    Info.log(f"数据库查询类型: {type(actual)} 查询结果: {actual}\n")
                    Info.log(f"Table assertion success: 表[{your_table}] → 字段[{column_name}] 期望值 等于 查询值，测试结束!\n")
                    return "actuals"
                elif expect_db is None:      # 期望值空
                    if len(actual[0]) > 1:   # 字段2列及以上。
                        arg = [row for row in actual]                   # 2行及以上数据时，返回所有数据 arg
                        actual = arg if len(arg) > 1 else actual[0]    # 只有1行数据，则返回第1行数据 actual[0][0]
                    elif len(actual[0]) == 1:  # 字段只有1列。
                        arg = [row[0] for row in actual]    # 2行及以上数据时，返回所有数据 arg 。目的：多行数据 与 接口返回的数据进行JSONpath操作后进行比较。
                        actual = arg if len(arg) > 1 else actual[0][0]     # 只有1行数据，则返回第1行数据 actual[0][0]
                    if isinstance(actual, (int, float, type)):  # 将数值转换为字符串
                        actual = f"{actual}"
                    Info.log(
                        f"Table assertion success! 字段[{column_name}] → 值[{actual}] exists in the 库[{self.db}] → 表[{your_table}]")
                    return actual  # 返回查询值
        except AssertionError as error:
            self.conn.rollback()
            raise Error.log(f"函数 assert_datatable() assertion error: {error}")
        # finally:
        #     # 关闭游标
        #     self.cur.close()
        #     # 关闭连接
        #     self.conn.close()
def assert_database(res, your_dbs=None, your_tables=None, column_names=None, expects=None, *args):
    '''
    数据库值断言
    :param res: 接口返回值
    :param your_dbs: 数据库
    :param your_tables: 数据库表名
    :param column_names: 列名         示例：   1、列表["id", "ces"]   2、元组("id", "ces")   3、字符串"user_base_id"
    :param expects: 期望值            示例：   1、元组 (892458041165238272,1)     2、字符串 "name"     3、整形 123
    :param args: 语句 where 数据值    示例：   ("user_base_id", "=", "892458041165238272"),("id", "like", "72%")
    :description:
        进入该函数的前提条件，已经将以下异常条件排出。所以只需考虑正常情况下的接口返回。
        401 403 404 5xx  未授权、禁止访问、资源不存在、服务异常。
        ConnectionError  建立连接时发生错误。
        Timeout          请求超时。
        TooManyRedirects 重定向次数过多。
    '''
    if responseJudgment(res) is True or responseJudgment(res) is None:
        # 实例化 数据库操作
        db = DbOperation(
            user_n=testuser,
            password_s=testpassword,
            port_n=testport,
            host_p=testhost,
            database_n=your_dbs)
        # 数据表断言
        ad = db.assert_datatable(
            your_tables,
            column_names,
            expects,
            *args)
        # if ad == 0:
        #     Info.log(f"数据库查询类型: {type(str(ad))} 查询结果: '0'\n")
        #     return "0"
        if ad is None:          # 用于查询结果为空时使用。
            Info.log(f"数据库查询类型: {type(str(ad))} 查询结果: 'None'\n")
            return 'None'
        if ad == "actuals":     # 用于传入期望值，并断言成功后。防止有内容输出。可忽略该句作用。
            pass
        else:
            try:
                ad = eval(f"{ad}") if isinstance(eval(f"{ad}"), (tuple, list, set, dict, enumerate, set)) else ad
            except:
                pass
            ad = f"{ad}" if isinstance(ad, (int, float)) else ad  # 将数值转换为字符串
            Info.log(f"数据库查询类型: {type(ad)} 查询结果: {ad}\n")
            return ad   # 返回查询值

def delete_sql(your_dbs, sql_s):
    """
    单表数据删除
    Args:
        column_name: 需要删除的字段名
        your_table: 表
        expect_db: 期望值
    Returns:
    """
    # time.sleep(1)
    db = DbOperation(
        user_n=testuser,
        password_s=testpassword,
        port_n=testport,
        host_p=testhost,
        database_n=your_dbs)
    db.delete_data(sql_s)

if __name__ == '__main__':
    do = DbOperation(user_n=testuser, password_s=testpassword, port_n=testport,host_p=testhost, database_n='medpot_miniapp')
    do.select_data("select user_id from tb_doctor_base_info where phone = '19828304890'")
    # print(do.assert_datatable("tb_recharge_record", ("user_base_id", "is_succes"), None,
    #                    ("user_base_id", "=", "892458041165238272"),("is_succes", "=", 1)))
    #
    # name = "待发货总数"
    # args = (("user_base_id", "=", "892458041165238272"),)
    # print(assert_database(
    #     "medpot_miniapp","tb_recharge_record", ("user_base_id", "is_succes"), None,
    #                    ("user_base_id", "=", "892458041165238272"),("is_succes", "=", 1)))
