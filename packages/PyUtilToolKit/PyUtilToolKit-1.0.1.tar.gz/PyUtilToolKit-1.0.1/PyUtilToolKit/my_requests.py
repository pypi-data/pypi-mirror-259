# -*- coding:utf-8 -*-
"""
@Time        : 2023/11/19
@File        : my_requests.py
@Author      : lyz
@version     : python 3
@Description :
"""
import json
import requests
from PyUtilToolKit.asserts.assert_base import assert_not_none, assert_equals, assert_containstring, assert_less
from PyUtilToolKit.log import *
from PyUtilToolKit.recursion import Recursive

class MyRequests:
    '''
    ① post、get请求
    ② 返回值断言

    正常情况下：
    状态码为 2xx：请求成功，并返回响应内容。
    状态码为 3xx：重定向请求。可以根据需要进行相应的处理。

    异常情况下：
    状态码为 401 Unauthorized：未授权请求。可能需要提供有效的身份验证信息。
    状态码为 403 Forbidden：禁止访问请求。可能需要更高级别的访问权限。
    状态码为 404 Not Found：请求的资源不存在。
    requests.exceptions.RequestException        异常：这是其他具体请求异常类的基类。
    requests.exceptions.HTTPError               异常：发生了 HTTP 错误。
    requests.exceptions.ConnectionError         异常：建立连接时发生错误。
    requests.exceptions.Timeout                 异常：请求超时。
    requests.exceptions.TooManyRedirects        异常：重定向次数过多。
    '''
    def __init__(self, session):
        self.session = session
    def post(self, url, data=None, jsons=None, headers=None, expect=None):
        '''
        post请求
        :param url: url
        :param data: 请求体格式为body-from
        :param jsons: 请求体格式为body-json
        :param headers: 请求头
        :param expect: 接口返回期望值
        :return:
        '''
        try:
            response = self.session.post(url, data=data, json=jsons, headers=headers)
            assert_response(responses=response, expects=expect, urls=url)
            Info.log(f"{url}\n{json.dumps(response.json(), indent=4, ensure_ascii=False)}")  # 日志打印返回结果
            Info.log(f"Post assertion success: {url}\n")
            return response.json()
        except json.decoder.JSONDecodeError:
            Warn.log(f"返回非JSON数据格式! {url}\n")
        except requests.exceptions.RequestException as error:
            raise Error.log(f"Post an error occurred: {error}\n")
        except AssertionError as error:
            raise Error.log(f"Post assertion failed: {error}\n")
    def get(self, url, params=None, headers=None, expect=None):
        '''
        get请求
        :param url: url
        :param params: 请求体格式
        :param headers: 请求头
        :param expect: 接口返回期望值
        :return:
        '''
        try:
            response = self.session.get(url, headers=headers, params=params)
            assert_response(responses=response, expects=expect, urls=url)
            Info.log(f"{url}\n{json.dumps(response.json(), indent=4, ensure_ascii=False)}")  # 日志打印返回结果
            Info.log(f"Get assertion success: {url}\n")
            return response.json()
        except json.decoder.JSONDecodeError:
            Warn.log(f"返回非JSON数据格式! {url}\n")
        except requests.exceptions.RequestException as error:
            raise Error.log(f"Get an error occurred: {error}\n")
        except AssertionError as error:
            raise Error.log(f"Get assertion failed: {error}\n")

    def get_dev(self, url, params=None, headers=None, expect=None):             # 调试用，请忽略
        try:                                                                    # 调试用，请忽略
            response = self.session.get(url, headers=headers, params=params)    # 调试用，请忽略
            assert_response(responses=response, expects=expect, urls=url)       # 调试用，请忽略
            return response.json()                                              # 调试用，请忽略
        except json.decoder.JSONDecodeError:
            Warn.log(f"返回非JSON数据格式! {url}")
        except requests.exceptions.RequestException as error:                   # 调试用，请忽略
            raise Error.log(f"Get an error occurred: {error}")                  # 调试用，请忽略
        except AssertionError as error:                                         # 调试用，请忽略
            raise Error.log(f"Get assertion failed: {error}")                   # 调试用，请忽略

    def upload(self, url, file=None, data=None, headers=None, expect=None):
        '''
        上传文件
        :param url: url
        :param data: 请求体格式为body-from
        :param file: 文件地址      file = {'file': open(ensure_path("\\uploadFile\\云药客公司\\业务推广\\基础数据管理-表单标题.xlsx"), 'rb')}
        :param headers: 请求头
        :param expect: 接口返回期望值
        :return:
        '''
        try:
            response = self.session.post(url, files=file, data=data, headers=headers)
            assert_response(responses=response, expects=expect, urls=url)
            Info.log(f"{url}\n{json.dumps(response.json(), indent=4, ensure_ascii=False)}")  # 日志打印返回结果
            Info.log(f"Assertion success: {url}\n")
            return response.json()
        except json.decoder.JSONDecodeError:
            Warn.log(f"返回非JSON数据格式! {url}\n")
        except requests.exceptions.RequestException as error:
            raise Error.log(f"An error occurred: {error}\n")
        except AssertionError as error:
            raise Error.log(f"Assertion failed: {error}\n")

def assert_response(responses, expects=None, urls=None):
    '''
    返回值断言
    :param responses: 返回值
    :param expects: 接口返回期望值
    :param urls: 地址
    :return:
    '''
    # 断言接口
    responses.raise_for_status()                                                            # 断言响应状态码为 4xx 或 5xx
    assert_not_none(url=urls, actual=responses.content)                                     # 断言返回值不为空
    assert_equals(url=urls, actual=responses.status_code, expect=200)                       # 断言HTTP响应码 200
    Recursive().recursive_get_values(responses.json())                  # 实例化 递归方法 获取返回数据
    assert_containstring(url=urls, actual=Recursive().toall(), expect=expects)              # 断言JSON响应内容是否符合预期

if __name__ == '__main__':
    pass