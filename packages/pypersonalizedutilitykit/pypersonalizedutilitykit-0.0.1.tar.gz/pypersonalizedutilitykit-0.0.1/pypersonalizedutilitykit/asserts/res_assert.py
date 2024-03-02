# -*- coding:utf-8 -*-
"""
@Time        : 2023/10/25 9:19
@File        : res_assert.py
@Author      : lyz
@version     : python 3
@Description :
"""
from yiXie_2_util.asserts.assert_base import *
from yiXie_2_util.recursion import Recursive

def assert_response(response, expect, expected_db_query_result=None, expected_response_time=2, url=None):
    response.raise_for_status()  # 如果请求不成功，抛出异常
    assert_not_none(url=url, actual=response.text)  # 断言返回值不为空
    assert_equals(url=url, actual=response.status_code, expect=200)  # 断言HTTP响应码 200
    rs = Recursive()  # 实例化
    rs.recursive_get_values(response.json())  # 断言JSON响应内容
    assert_containstring(url=url, actual=rs.toall(), expect=expect)
    # 断言数据库值存在
    # if expected_db_query_result is not None:
    #     conn = pymysql.connect(host='localhost', user='root', password='password', db='database')
    #     cursor = conn.cursor()
    #     cursor.execute(expected_db_query_result)
    #     result = cursor.fetchone()
    #     for field, expected_value in expected_db_query_result.items():
    #         assert result[field] == expected_value
    #     cursor.close()
    #     conn.close()
    assert_less(url=url,actual=response.elapsed.total_seconds(), expect=expected_response_time)