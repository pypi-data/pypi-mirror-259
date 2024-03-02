# -*- coding:utf-8 -*-
"""
@Time        : 2023/11/24
@File        : notify.py
@Author      : lyz
@version     : python 3
@Description :
"""
import time
from enum import Enum, unique

now_time_day = time.strftime("%Y-%m-%d", time.localtime())

project_name = f"一蟹科技项目-{now_time_day}-"

notification_type = "0"    # 报告通知类型：0: 不发送通知 1：钉钉 2：邮箱通知
                         # 支持同时发送多个通知，如多个，则用逗号分割， 如 "1,2"

email={
  "send_user": "yezhao.liu@medcrab.com",
  "email_host": "smtp.qiye.aliyun.com",
  "stamp_key": "vAXvib18O7akTCax",                  # 自己到邮箱中配置第三方   QQ邮箱：srnscqyelpqlbgih
  "send_list": "yezhao.liu@medcrab.com"
  # "send_list": "yezhao.liu@medcrab.com,yushu.zhao@medcrab.com,"
  #              "yanwen.liang@medcrab.com,yong.wang@medcrab.com,yifan.shen@medcrab.com"          # 收件人改成自己的邮箱
}
class NotificationType(Enum):
    """ 选择自动化通知方式，钉钉、邮箱 """
    DEFAULT = '0'
    DING_TALK = '1'
    EMAIL = '2'

if __name__ == '__main__':
    print(notification_type.split(","))