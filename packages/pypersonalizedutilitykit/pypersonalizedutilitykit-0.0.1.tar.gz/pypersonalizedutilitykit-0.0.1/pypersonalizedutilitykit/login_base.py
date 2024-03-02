# -*- coding: utf-8 -*-
"""
# File       : login_base.py
# Time       ：2023/10/21
# Author     ：lyz
# version    ：python 3
# Description：
"""
from datetime import datetime
from yiXie_1_config.hostUrl.hostUrl_login import *
from yiXie_1_config.tokenConfig.token_manage import WriteYaml
from yiXie_2_util.log import Info
import requests

from yiXie_3_func.xuanHuMini_func.woDe_func.geRenXinXi_func import GeRenXinXi


class SaasLogin:
    def __init__(self):
        self.session = requests.session()
    def saaslogin(self, user, pwd, plant=None):
        """
        用户登录       适用于 后台/公司/监理     "houTai","firm","jianLi"
        :param user: 获取接口用户名
        :param pwd: 获取密码
        :param plant: 平台（后台/公司/监理）
        :return: 返回响应体
        """
        data_login = {"accountName": user, "password": pwd}
        response = self.session.post(url=userAccountLogin, data=data_login, verify=False)   # 登录请求
        param = {"callback": "{}".format(orgg)}
        requests.get(url=container, params=param, headers=self.session.cookies)   # 登录重定向请求
        response.raise_for_status()  # 如果请求不成功，抛出异常
        token(response, plant) if plant is not None else True       # 如果 plant存在，获取token
        Info.log("Token过期时间:{}".format(datetime.fromtimestamp(response.json()["data"]["expireDate"] / 1000)))
        Info.log(f"Login success! {userAccountLogin} & {container}")
        tokenValue = response.json()["data"]["tokenValue"]      # 获取登录接口响应体中的token值
        self.session.headers.update({"token": tokenValue})      # 在session中添加token
        return self.session

# class YykWebLogin:
#     def __init__(self):
#         self.session = requests.session()
#     def yykweblogin(self, user, pwd, plant=None):
#         """
#         用户登录       适用于 云药客web        "yykWeb"                       # 需要优化，只是将上面复制下来了
#         :param user: 获取接口用户名
#         :param pwd: 获取密码
#         :param plant: 平台（云药客web）
#         :return: 返回响应体
#         """
#         url = HostEnv().host_login("user") + login_url["login"]  # host_("xxx") 在 config.py中配置
#         data_login = {"accountName": user, "password": pwd}
#         response = self.session.post(url, data=data_login)
#         response.raise_for_status()  # 如果请求不成功，抛出异常
#         token(response, plant) if plant is not None else True  # 如果 plant存在，获取token
#         Info.log("Token过期时间:{}".format(datetime.fromtimestamp(response.json()["data"]["expireDate"] / 1000)))
#         # Info.log(f"Url {userAccountLogin} & {container} login success!")
#         tokenValue = response.json()["data"]["tokenValue"]  # 获取登录接口响应体中的token值
#         self.session.headers.update({"token": tokenValue})  # 在session中添加token
#         return self.session
class XuanHuLogin:
    def __init__(self):
        self.session = requests.session()
    def xuanHuMiniLogin(self, user, pwd, plant=None):
        """
        用户登录       适用于 悬壶小程序            "xuanHuMini"
        :param user: 获取接口用户名
        :param pwd: 获取密码
        :param plant: 平台（悬壶）
        :return: 返回响应体
        """
        data_login = {"unionId": user, "signature": pwd}
        response = self.session.post(url=userWechatMiniLogin, data=data_login, verify=False)
        response.raise_for_status()  # 如果请求不成功，抛出异常
        token(response, plant) if plant is not None else True  # 如果 plant存在，获取token
        Info.log("Token过期时间:{}".format(datetime.fromtimestamp(response.json()["data"]["expireDate"] / 1000)))
        Info.log(f"Login success! {userWechatMiniLogin}")
        tokenValue = response.json()["data"]["tokenValue"]  # 获取登录接口响应体中的token值
        self.session.headers.update({"token": tokenValue})  # 在session中添加token
        return self.session

class YykAppLogin:
    def __init__(self):
        self.session = requests.session()
    # def yykapplogin(self, user, pwd, plant=None):
    #     """
    #     用户登录       适用于 云药客app       "yykApp"                        # 需要优化，只是将上面复制下来了
    #     :param user: 获取接口用户名
    #     :param pwd: 获取密码
    #     :param plant: 平台（云药客app）
    #     :return: 返回响应体
    #     """
    #     url = HostEnv().host_login("user") + login_url["login"]  # host_("xxx") 在 config.py中配置
    #     data_login = {  # body 参数
    #         "accountName": user,
    #         "password": pwd
    #     }
    #     response = self.session.post(url, data=data_login)
    #     response.raise_for_status()  # 如果请求不成功，抛出异常
    #     token(response, plant) if plant is not None else True  # 如果 plant存在，获取token
    #     Info.log("Token过期时间:{}".format(datetime.fromtimestamp(response.json()["data"]["expireDate"] / 1000)))
    #     # Info.log(f"Url {userWechatMiniLogin} login success!")
    #     tokenValue = response.json()["data"]["tokenValue"]  # 获取登录接口响应体中的token值
    #     self.session.headers.update({"token": tokenValue})  # 在session中添加token
    #     return self.session
class TimedTaskLogin:
    def __init__(self):
        self.session = requests.session()
    def timedTaskLogin(self, user, pwd):
        """
        用户登录       适用于 定时任务     "timedTask"
        :param user: 获取接口用户名
        :param pwd:  获取密码
        :param plant: 平台 定时任务
        :return: 返回响应体
        """
        data_login = {"userName": user, "password": pwd}
        response = self.session.post(url=timedTaskLogin, data=data_login, verify=False)
        requests.get(url=timedTaskToLogin, headers=self.session.cookies)
        response.raise_for_status()     # 如果请求不成功，抛出异常
        Info.log(f"Login success! {timedTaskLogin} & {timedTaskToLogin}")
        return self.session

def token(res, plant):
    '''
    将登录的token写入yaml文件中
    :param res: 返回值
    :param plant: 后台？公司？监理？等...
    :return:
    '''
    if (plant == "houTai" or plant == "firm" or plant == "jianLi" or plant == "houTai" or plant == "yykWeb"
            or plant == "xuanHuMini" or plant == "xuanHuWeb" or plant == "yykApp" or plant == "timedTask"):
        res_token = res.json()["data"]["tokenValue"]  # 获取 token
        WriteYaml(plant, res_token)  # 将 token 写入yaml文件
        Info.log(f'token_{plant}值写入yaml文件，成功！')
    else:
        raise Exception('请输入:正确名称!')

if __name__ == '__main__':
    a = XuanHuLogin().xuanHuMiniLogin("obGrgv2jyS-Z48-US8Gnhem_4kSI","4117C1A5E2B35F193F3990361EDAB27E")
    GeRenXinXi(a).user_base_info()