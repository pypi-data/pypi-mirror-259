# -*- coding:utf-8 -*-
"""
@Time        : 2022/4/25 9:19
@File        : operation_json.py
@Author      : lyz
@version     : python 3
@Description :
"""
import os, json

from yiXie_2_util.pathSetting import ensure_path


class OperationJson:

    def __init__(self, json_path):
        self.json_path = ensure_path(json_path)

    def read_json(self):
        '''
        在json中读取数据
        :return:
        '''
        if os.path.exists(self.json_path):
            with open(self.json_path, 'rb') as fp:
                content = fp.read()
            try:
                content_str = content.decode('utf-8')
            except UnicodeDecodeError:
                content_str = content.decode('gbk')
            return json.loads(content_str)
        else:
            raise FileNotFoundError('json文件不存在 or 路径错误!')
    def write_json(self, data):
        '''
        向json中写入数据
        :param data:数据
        :return:
        '''
        try:
            with open(self.json_path, 'w+', encoding='utf-8') as fp:
                json.dump(data, fp, ensure_ascii=False, indent=4)
        except Exception:
            raise IOError('写入 json 文件失败！')
    def value(self, key):
        '''
        获取指定键对应的值
        :param key:键
        :return:
        data = [
            [None,111,"订单列表查询成功"],
            ['185128', '805', "密码错误"],
            ['185128', '805', "操作成功"],
            ['185128', '805', "登录成功"]
        ]
        '''
        data = self.read_json()
        return data.get(key)
    def values(self, key):
        '''
        获取指定键对应的值
        :param key:键
        :return:    注意：values 与 value 的区别。values 有两层列表!
        data = [
            ["单张纸质发票", [YeCainYiTiModel, "单张纸质发票金额不能超过10万元"]],
            ["电子开票金额", [YeCainYiTiModel, "success"]],
            ["15张发票 ", [YeCainYiTiModel, "success"]],
            [成功,["factoryName"]]
        ]
        '''
        data = self.read_json()
        results = []
        for item in data.get(key):
            if isinstance(item[1], list) and len(item[1]) == 1:
                results.append(item[1][0])  # 单个值 ["factoryName"]        [成功,["factoryName"]]
            else:
                results.append(item[1])  # 多个值 [1,"factoryName"]       [成功,[1,"factoryName"]]
        return results

if __name__ == '__main__':
    pass
    # test = [
    #     (None,111,"订单列表查询成功"),
    #     ('18512805719', '805718', "密码错误"),
    #     ('18512805718', '805718', "操作成功"),
    #     ('18512805719', '805718', "登录成功")
    # ]
    # data = OperationJson(
    #     "\\yiXie_5_test_weekday\\test_firm_weekday\\test_yeWuZhongXin_weekday\\test_huiKuanGuanLi_weekday.json").value("bu_men_xin_xi")
    # results = []
    # for item in data:
    #     print("1", item[1], type(item[1]))
    #     if isinstance(item[1], list) and len(item[1]) == 1:
    #         print("2", item[1], type(item[1]))
    #         results.append(item[1][0])
    #     else:
    #         print("3", item[1], type(item[1]))
    #         results.append(item[1])
    # print(results, type(results))
    # data1 = OperationJson(
    #     "\\yiXie_5_test_weekday\\test_firm_weekday\\test_yeWuZhongXin_weekday\\test_huiKuanGuanLi_weekday.json").value(
    #     "bu_men_xin_xi2")
    # print(data1, type(data1))
    # print(ensure_path("\\yiXie_5_test_weekday\\test_xuanHuMin\\test_woDe_weekday\\test_woDe_weekday.json"))
    # # print(OperationJson("\\yiXie_5_test_weekday\\test_xuanHuMin\\test_woDe_weekday\\test_woDe_weekday.json").value("ti_xian_ji_lu"))
    # print(os.path.exists(ensure_path("\\yiXie_5_test_weekday\\test_xuanHuMin\\test_woDe_weekday\\test_woDe_weekday.json")))
    # "\\yiXie_5_test_weekday\\test_xuanHuMini_weekday\\test_woDe_weekday\\test_woDe_weekday.json"