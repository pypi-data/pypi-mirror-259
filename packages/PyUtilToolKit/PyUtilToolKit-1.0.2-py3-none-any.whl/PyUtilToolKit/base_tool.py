# -*- coding:utf-8 -*-
"""
@Time        : 2024/1/12
@File        : base_tool.py
@Author      : lyz
@version     : python 3
@Description : 存放自己需要的功能
"""
import json
import os
from hamcrest import assert_that, equal_to
from jsonpath import jsonpath
from PyUtilToolKit.log import *
from datetime import datetime, timedelta
import datetime
from PyUtilToolKit.pathSetting import root_path


def clean_pyc_files():
    """
    清除当前目录及其子目录中的Python编译文件
    Args:
        directory: 路径
    Returns:
    """
    for root, dirs, files in os.walk(root_path()):
        for file in files:
            if file.endswith(".pyc"):
                path = os.path.join(root, file)
                os.remove(path)
                print(f"Removed: {path}")


'''--------------------------------------------------分割线--------------------------------------------------'''

def specifyTime(days=0, hours=0, minutes=0, seconds=0):
    """
    指定时间（在当前时间基础上指定时间）
    Args:
        days: +天
        hours: +时
        minutes: +分
        seconds: +秒
    Returns:
    """
    # 获取当前时间
    current_time = datetime.datetime.now()
    # 将时间格式化为只包含秒的字符串
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    # 将字符串转换回datetime对象
    current_time = datetime.datetime.strptime(formatted_time, '%Y-%m-%d %H:%M:%S')
    # 增加1天、1小时、1分钟和1秒钟
    new_time = current_time + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    # 打印新的时间
    return new_time.strftime('%Y-%m-%d %H:%M:%S')


'''--------------------------------------------------分割线--------------------------------------------------'''
def deleteOldLogs(log_directory=ensure_path("\\yiXie_8_log"), days=3):
    """
    自动删除X天前的log文件
    Args:
        log_directory:指定log目录
        days:删除的天数
    Returns:
    """
    # 获取当前时间戳
    current_time = time.time()
    # 计算3天前的时间戳
    three_days_ago = current_time - (days * 24 * 60 * 60)
    # 遍历log目录中的所有文件
    for filename in os.listdir(log_directory):
        file_path = os.path.join(log_directory, filename)
        # 判断文件是否为普通文件且最后一次修改时间早于三天前
        if os.path.isfile(file_path) and os.path.getmtime(file_path) < three_days_ago:
            # 删除文件
            os.remove(file_path)
            Info.log(f"已删除文件: {file_path}")


'''--------------------------------------------------分割线--------------------------------------------------'''
def responseValue(res, key = None):
    """
    获取接口返回值       主要用在查询 列表/明细 等
    Args:
        res: 接口返回值
        days: key值  "$.data.total"  "$.data.list[*].id"
    Returns: 一般对返回值校验3中方式   1、re is True     2、re == 'None'       3、re == data
    """
    try:
        if responseJudgment(res) is True:   # 进行返回值断言
            if key is None:
                Info.log(f"JsonPath值为空，返回True\n")
                return True
            else:
                value = jsonpath(res, key)  # 获取接口返回值
                if value:   # 有返回值
                    # 没有[*] 输出total[0]，有[*] 输出total
                    data = value[0] if "[*]" not in key else (value[0] if len(value) == 1 else value)
                    data = f"{data}" if isinstance(data, (int, float)) else data  # 将数值转换为字符串
                    Info.log(f"接口取值类型: {type(data)} 取值结果: {data} \n")
                    return data
                elif value is False:   # 无返回值
                    Info.log(f"接口取值结果: 'None' \n")
                    return 'None'  # 返回字符串"None" 是因为 后边会遇到 if 非空判断。
        elif responseJudgment(res) is False:    # 不进行返回值断言
            Info.log(f"不进行数据库值断言，测试结束! 接口响应结果 {res} ")
    except:
        raise Error.log(f"接口key: [{key}] error !")


'''--------------------------------------------------分割线--------------------------------------------------'''
def responseValueDev(res, key = None):
    '''调试用，可忽略'''
    try:
        if responseJudgment(res) is True:   # 进行返回值断言
            if key is None:
                Info.log(f"JsonPath值为空，返回True\n")
                return True
            else:
                value = jsonpath(res, key)  # 获取接口返回值
                if value:   # 有返回值
                    # 没有[*] 输出total[0]，有[*] 输出total
                    data = value[0] if "[*]" not in key else (value[0] if len(value) == 1 else value)
                    data = f"{data}" if isinstance(data, (int, float)) else data  # 将数值转换为字符串
                    return data
                elif value is False:   # 无返回值
                    Info.log(f"接口取值结果: 'None' \n")
                    return 'None'  # 返回字符串"None" 是因为 后边会遇到 if 非空判断。
        elif responseJudgment(res) is False:    # 不进行返回值断言
            Info.log(f"不进行数据库值断言，测试结束! 接口响应结果 {res} ")
    except:
        raise Error.log(f"接口key: [{key}] error !")

'''--------------------------------------------------分割线--------------------------------------------------'''
def responseJudgment(res):
    """
    接口返回值判断         在responseValue()中调用
    Args:
        res: 接口返回值
    Returns:
    """
    try:
        code = jsonpath(res, "$.code")  # 获取接口返回值 code
        if int(code[0]) == 1 or int(code[0]) == 200:   # 进行返回值断言
            return True
        elif int(code[0]) == -1:  # 不进行返回值断言
            return False            # 返回False
        elif int(code[0]) == 1 or int(code[0]) == 200 or int(code[0]) == -1:
            raise Error.log(f"接口响应错误: {res}")
    except TypeError:
        Warn.log(f"返回非JSON数据格式! {res}")


'''--------------------------------------------------分割线--------------------------------------------------'''
def comparApiDb(api, db):
    """
    接口&数据库数值比较
    Args:
        api: 接口返回数据
        db: 数据库返回数据
    Returns:
    """
    if api:     # 接口不为False，才进行与数据库值比较
        if db:
            if isinstance(api, (list, tuple, dict, set)):  # 列表、元组、字典、集合
                api = sorted(api)
            if isinstance(db, (list, tuple, dict, set)):   # 列表、元组、字典、集合
                db = sorted(db)
            assert_that(api, equal_to(db), reason=f"[接口返回参数值: {api} 与 数据库查询值: {db} 数据不等，请检查数据!")
            Info.log(f"[接口取值结果 等于 数据库查询结果，测试结束!")
        else:
            raise Error.log(f"[数据库查询值:{db} 返回为False，请检查数据!")


'''--------------------------------------------------分割线--------------------------------------------------'''
def sqlArg(field, operator, value, condit=None):
    """
    sql语句 条件参数
    Args:  sqlArg("is_delete", "=", 1)
        field: 字段
        operator: 操作符号 "like、=、between"
        value: 值 "and"
        condit: 条件 "and" "or" ")"
    Returns:
    """
    # operator 与 value 都含有None 的情况
    if (("NONE" in str(operator).upper() and "NONE" in str(value).upper()) or
            ("NONE" in str(operator).upper() or "NONE" in str(value).upper())):
        tup = (field, str(operator), str(value), str(condit))
        return tup
    # between
    elif "BETWEEN" in str(operator).upper() and "AND" in str(value).upper():
        tup = (field, operator, value, str(condit))
        return tup
    elif (("BETWEEN" in str(operator).upper() and "AND" not in str(value).upper()) or
          ("BETWEEN" not in str(operator).upper() and "AND" in str(value).upper())):
        raise Exception("请检查 between and 语句!")
    # like
    elif "LIKE" in str(operator).upper():
        tup = (field, str(operator), str(f"%{value}%"), str(condit))
        return tup
    # 正常情况
    else:
        tup = (field, operator, value, str(condit))
        return tup


'''--------------------------------------------------分割线--------------------------------------------------'''
def covertStr(actual):
    '''
    将数据库查询值转换为字符串类型
    Args:
        actual: 数据库查询值
    Returns:
    '''
    actuals = actual[0][0]
    try:    # 捕获非基本的数据类型值
        # if isinstance(eval(f"{actuals}"), (tuple, list, set, dict, enumerate, set)):   # 非字符串
        #     return tuple(tuple(str(col) if isinstance(col, int) else col for col in row) for row in actual)
        if isinstance(actuals, datetime.datetime):  # 时间datetime类型
            return tuple(tuple(str(col.strftime('%Y-%m-%d %H:%M:%S')) for col in row) for row in actual)
        else:
            return tuple(tuple(str(col) if isinstance(col, int) else col for col in row) for row in actual)
    except Exception:
        pass
    if isinstance(actuals, datetime.datetime):  # 时间datetime类型
        return tuple(tuple(str(col.strftime('%Y-%m-%d %H:%M:%S')) for col in row) for row in actual)
    else:
        return tuple(tuple(str(col) if isinstance(col, int) else col for col in row) for row in actual)


if __name__ == '__main__':
    deleteOldLogs()
    clean_pyc_files()
    # a = (('转账公司全称-接口测试',), ('转账公司全称-接口测试',), ('转账公司全称-接口测试',), ('转账公司全称-接口测试',), ('转账公司全称-接口测试',), ('转账公司全称-接口测试',), ('转账公司全称-接口测试',))
    # covertStr(a)
    # print(specifyTime(seconds=1) > "2024-02-07 17:55:07")
    # print(sqlArg("id", "=", None))
    # aa = [{"actualAmount": 45000, "discount": 90, "rechargeAmount": 50000},
    #       {"actualAmount": 91000, "discount": 91, "rechargeAmount": 100000}]
    # print(covertStr(aa))
    # print(len(aa[0]))
    # a = {
    #     "code": 1,
    #     "data": {
    #         "businessNo": "950810156550975488",
    #         "orderId": "950810156625489920",
    #         "orderNo": "202402021781775466"
    #     },
    #     "message": "success",
    #     "stateCode": "000000"
    # }
    # value = jsonpath(a, "$.data.businessNo")  # 获取接口返回值
    # print(type(value))
    # print(responseJudgment(a))
    # businessNo = responseValue(a, "$.data.businessNo")
    # orderId = responseValue(a, "$.data.orderId")
    # print(businessNo,orderId)
    # print(clean_pyc_files())


    # b = (947834767895683072, 1)
    # print(type(b[1]))