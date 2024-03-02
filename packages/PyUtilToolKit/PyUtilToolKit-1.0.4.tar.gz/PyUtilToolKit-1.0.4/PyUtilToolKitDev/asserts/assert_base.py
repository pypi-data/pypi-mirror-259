# -*- coding:utf-8 -*-
"""
@Time        : 2023/10/28 
@File        : assert_base.py
@Author      : lyz
@version     : python 3
@Description :
"""
from hamcrest import *

def assert_db(actual):
    '''
    断言匹配对象不为(),给数据库断言专用
    :param actual:
    :return:
    '''
    assert_that(actual, is_not(()), reason="reason was 'Expected value is not none!'")

def assert_not_none(actual, url=None):
    '''
    断言匹配对象不为空
    :param actual:
    :return:
    '''
    assert_that(actual, is_not(None), reason=f"url was '{url}'\nreason was 'Expected value is not none!'")

def assert_equals(actual,expect=None, url=None):
    '''
    断言匹配相等对象
    :param actual:
    :param expect:
    :return:相等则不抛出异常，不相等则抛出异常
    '''
    if expect is not None:
        assert_that(actual, equal_to(expect),
                reason=f"url was '{url}'\nreason was 'Expected value is not equal to the actual value!'")
    else:
        pass

def assert_containstring(actual, expect=None, url=None):
    '''
    断言匹配字符串的一部分
    :param actual:
    :param expect:
    :return:
    '''
    if expect is not None:
        assert_that(actual, contains_string(str(expect)),
                reason=f"url was '{url}'\nreason was 'Expected value not contained in actual value!'")
    else:
        pass

def assert_less(actual, expect=None, url=None):
    '''
    断言数字小于预期
    :param actual:
    :param expect:less_than
    :return:
    '''
    if expect is not None:
        assert_that(actual, less_than(expect),
                reason=f"url was '{url}'\nreason was 'Actual value is greater than or equal to the expected value!'")
    else:
        pass

if __name__ == '__main__':
    # assert_containstring(url=None, actual='123', expect='3')
    print(assert_containstring("323"))