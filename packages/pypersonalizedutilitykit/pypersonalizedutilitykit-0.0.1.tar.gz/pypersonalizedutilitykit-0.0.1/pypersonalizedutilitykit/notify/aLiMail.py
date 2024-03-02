# -*- coding:utf-8 -*-
"""
@Time        : 2023/11/23
@File        : aLiMail.py
@Author      : lyz
@version     : python 3
@Description :
"""
from datetime import datetime
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from yiXie_2_util.base_tool import deleteOldLogs
from yiXie_2_util.notify.notice import email, now_time_day, project_name
from yiXie_2_util.notify.report import TestReportWrapper
from yiXie_2_util.pathSetting import ensure_path
import smtplib

from yiXie_2_util.touch_file import touch_excel


class SendEmail:

    def __init__(self):
        self.trw = TestReportWrapper()
    """ 发送邮箱 """
    @classmethod
    def send_mail(cls, user_list: list, sub, content: str) -> None:
        """
        @param user_list: 发件人邮箱
        @param sub:
        @param content: 发送内容
        @return:
        """
        user = "lyz" + "<" + email["send_user"] + ">"
        multipart = MIMEMultipart()
        multipart['Subject'] = sub
        multipart['From'] = user
        multipart['To'] = ";".join(user_list)
        # 添加邮件正文
        text = MIMEText(content, _subtype='plain', _charset='utf-8')
        multipart.attach(text)
        # 添加附件
        with open(ensure_path("\\yiXie_9_report\\result_report.xlsx"), 'rb') as f:
            attachment = MIMEApplication(f.read(), _subtype='xlsx')
            attachment.add_header('Content-Disposition', 'attachment',
                                  filename=f'一蟹科技项目-接口自动化测试-{now_time_day}-Report.xlsx')
            # attachment.add_header('Content-Type', 'text/html')
            # attachment.add_header('Content-Transfer-Encoding', 'base64')
            multipart.attach(attachment)
        server = smtplib.SMTP()
        server.connect(email["email_host"])
        server.login(email["send_user"], email["stamp_key"])
        server.sendmail(user, user_list, multipart.as_string())
        server.close()

    def error_mail(self, error_message: str) -> None:
        """
        执行异常邮件通知
        @param error_message: 报错信息
        @return:
        """
        ema = email["send_list"]
        user_list = ema.split(',')  # 多个邮箱发送，email文件中直接添加  'xxxxxx74@qq.com'
        sub = project_name + "接口自动化执行异常通知"
        content = f"\t{now_time_day}接口自动化执行中发现程序异常，请悉知!报错信息如下:\n{error_message}"
        self.send_mail(user_list, sub, content)

    def send_main(self) -> None:
        """
        发送邮件
        :return:
        """
        ema = email["send_list"]    # 基本信息配置
        user_list = ema.split(',')  # 多个邮箱发送，email文件中直接添加  'xxxxxx74@qq.com'
        sub = project_name + "接口自动化测试报告"        #         错误: {self.trw.get_summary()['errors']}
                                                      #         跳过: {self.trw.get_summary()['skipped']}
        content = f"""
        各位同事, 大家好:
        \t{now_time_day}-接口自动化测试用例执行完毕，以下为测试统计数据，请查阅~
        总计: {self.trw.get_summary()['total']}
        通过: {self.trw.get_summary()['passed']}
        失败: {self.trw.get_summary()['failed']}
        通过率: {self.trw.get_summary()['pass_rate']}%
        运行时长: {self.trw.get_summary()['elapsed_time']}
        结束时间: {self.trw.get_summary()['timestamp']}
        ---------------------------------------------------------------------------------------------------------------
        详细情况可查看附件xlsx文件，或登录Jenkins平台查看，非相关人员可忽略此消息，谢谢~
        Jenkins地址：http://192.168.0.212:8080/
        """
        time.sleep(2)
        self.send_mail(user_list, sub, content)

    def check_file_exists(self):
        '''
        轮询检查文件是否生成
        :param filepath:文件地址
        :param timeout:超时时间
        :return:
        '''
        while True:
            time.sleep(2)
            if (os.path.exists(ensure_path("\\yiXie_9_report\\report.html"))
                    and os.path.exists(ensure_path("\\yiXie_9_report\\result.xml"))):
                touch_excel()     # 创建excel报告
                self.send_main()
                # 删除测试报告文件
                # os.remove(ensure_path("\\yiXie_9_report\\result.xml"))
                deleteOldLogs()  # 删除日志
                break
            elif time.time() > datetime.strptime(self.trw.get_summary()['timestamp'],
                                                 "%Y-%m-%dT%H:%M:%S.%f").timestamp() + 60:
                self.error_mail('系统未生成 report.html or result.xml 文件!')
                if os.path.exists(ensure_path("\\yiXie_9_report\\report.html")):
                    os.remove(ensure_path("\\yiXie_9_report\\report.html"))
                elif os.path.exists(ensure_path("\\yiXie_9_report\\result.xml")):
                    os.remove(ensure_path("\\yiXie_9_report\\result.xml"))
                break
            time.sleep(2)


if __name__ == '__main__':
    SendEmail().check_file_exists()




