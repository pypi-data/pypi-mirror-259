# -*- coding:utf-8 -*-
"""
@Time        : 2023/10/25 9:19
@File        : pathSetting.py
@Author      : lyz
@version     : python 3
@Description :
"""
import os
from typing import Text

def root_path():
    """ 获取 根路径 """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path

""" 当前路径 """
relative_path = os.sep.join(os.getcwd().split("\\"))

def ensure_path(path: Text) -> Text:
    """兼容 windows 和 linux 不同环境的操作系统路径 """
    if "/" in path:
        path = os.sep.join(path.split("/"))

    if "\\" in path:
        path = os.sep.join(path.split("\\"))

    return root_path() + path

if __name__ == '__main__':
    print(ensure_path("\\yiXie_5_test_weekday\\test_xuanHuMin\\test_woDe_weekday\\test_woDe_weekday.json"))
