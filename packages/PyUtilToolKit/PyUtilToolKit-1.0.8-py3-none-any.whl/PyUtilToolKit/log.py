# -*- coding:utf-8 -*-
"""
# File       : log.py
# Time       ：2023/1/21 13:45
# Author     ：lyz
# version    ：python 3
# Description：
"""
import logging
import time
from PyUtilToolKit.pathSetting import ensure_path
class AutoLog:

    def __init__(self, filename, level_param):
        self.filename = filename
        self.level_param = level_param

    def logs(self, message):
        self.logger = logging.getLogger()
        try:
            fh = logging.FileHandler(filename=self.filename, encoding="utf-8")  # 创建文件
            ch = logging.StreamHandler()  # 创建控制台
            fm = logging.Formatter('[%(levelname)-4s][%(asctime)s][%(message)s')  # 格式化

            fh.setFormatter(fm)  # 对文件格式
            ch.setFormatter(fm)  # 对控制台格式
            self.logger.addHandler(fh)  # 文件句柄加入logger
            self.logger.addHandler(ch)  # 控制台句柄加入logger
            self.logger.setLevel(level=logging.INFO)  # 设置打印级别

            if self.level_param == 'debug':
                self.logger.debug(message)
            elif self.level_param == 'info':
                self.logger.info(message)
            elif self.level_param == 'error':
                self.logger.error(message)
            elif self.level_param == 'warning':
                self.logger.warning(message)

            self.logger.removeHandler(fh)  # 删除文件句柄
            self.logger.removeHandler(ch)  # 移除控制台对象
        except:
            print('file exception')
        # finally:
        #     fh.close()

now_time_day = time.strftime("%Y-%m-%d", time.localtime())
Info = AutoLog(ensure_path(f"\\yiXie_8_log\\info-{now_time_day}.log"), level_param='info')
Warn = AutoLog(ensure_path(f"\\yiXie_8_log\\warn-{now_time_day}.log"), level_param='warning')
Error = AutoLog(ensure_path(f"\\yiXie_8_log\\error-{now_time_day}.log"), level_param='error')
# WARNING = AutoLog(ensure_path_sep(f'\\yiXie_8_log\\warning-{now_time_day}.log'))

if __name__ == '__main__':
    Error.logs("测试")
    Info.logs("测试1")

'''--------------------------------------------------分割线--------------------------------------------------'''
