# -*- coding:utf-8 -*-
"""
@Time        : 2023/10/28
@File        : operation_cash.py
@Author      : lyz
@version     : python 3
@Description :
"""
import os.path
from typing import Any

_cache_data = {}

class OperationCache:


    @classmethod
    def read_cache(cls, path):
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    return f.read()
            except Exception as e:
                raise IOError("读取缓存文件失败！")
        else:
            print(111)

    @classmethod
    def write_cache(cls, path, data):
        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(data)
        except Exception as e:
            raise IOError("写入缓存文件失败！")

    @classmethod
    def update_cache(cls, name: str, value: str) -> bool:
        try:
            _cache_data[name] = value
            return True
        except Exception as e:
            raise ValueError('更新缓存失败') from e

    @classmethod
    def get_cache(cls, name: str) -> Any:
        if name in _cache_data.keys():
            return _cache_data[name]
        raise AttributeError("无该缓存名，请检查缓存名是否正确")