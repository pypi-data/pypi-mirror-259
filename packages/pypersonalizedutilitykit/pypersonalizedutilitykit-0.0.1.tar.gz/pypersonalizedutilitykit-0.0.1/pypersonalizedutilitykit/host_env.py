# -*- coding:utf-8 -*-
"""
@Time        : 2023/10/25 9:19
@File        : host_env.py
@Author      : lyz
@version     : python 3
@Description :
"""

from yiXie_2_util.log import Error

class HostEnv:

    def __init__(self, chose=1):
        '''
        选择环境
        :param chose:   1.测试环境  2.预发环境
        '''
        self.env = None    # 选择环境头
        if chose == 1:
            self.env = "http://test"
        elif chose == 2:
            self.env = "https://pre"
        else:
            raise Error.log(chose)
    def host_login(self, host_, address_=None):
        '''
        登录
        '''
        if address_ is None:
            return f"{self.env}{host_}"
        else:
            return f"{self.env}{host_}{address_}"
    def host_xuanHuMini(self, host_, address_=None):
        '''
        悬壶小程序
        '''
        if self.env == "http://test":
            envs = "https://test"
            return f"{envs}{host_}{address_}"
        else:
            return f"{self.env}{host_}{address_}"

    def host(self, host_, address_):
        '''
        通用 （包含：云药客公共、云药客后台、云药客公司、云药客监理、yykApp、云药客Web、悬壶web、悬壶后台、定时任务、公共基础服务）
        '''
        return f"{self.env}{host_}{address_}"

if __name__ == '__main__':
    print(HostEnv(1).host_login('opt'))