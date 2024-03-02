# -*- coding:utf-8 -*-
"""
@Time        : 2023/10/28 23:02
@File        : recursion.py
@Author      : lyz
@version     : python 3
@Description :
"""


class Recursive:
    toal = []
    def __init__(self):
        '''
        递归获取请求响应值
        '''
        self.tmp = []

    # def rs(self, ite):
    #     '''
    #     表达式的方式，与recursive_get_values 作用相同。      法二：
    #     :param ite:
    #     :return:
    #     '''
    #     return (list(Recursive().rs(value)) if isinstance(value, dict) else str(value) for key, value in
    #             ite.items())

    def recursive_get_values(self, dic):
        """
        获取value
        Args:
            dic: 接口返回值
        Returns:
        """
        for key, value in dic.items():
            if isinstance(value, dict):
                self.recursive_get_values(value)
            else:
                Recursive().toal.append(str(value))

    def toall(self):
        """使用/将value连接起来"""
        self.tmp = list(Recursive().toal)
        Recursive().toal.clear()
        return "/".join(self.tmp)