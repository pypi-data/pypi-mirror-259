# -*- coding:utf-8 -*-
"""
# File       : touch_csv.py
# Time       ：2023/1/21
# Author     ：lyz
# version    ：python 3
# Description：
"""
import csv
import datetime
import numpy

def Unicode1():
    num1 = numpy.random.randint(1, 10000000, 1)
    return num1

def Unicode2():
    first_name = ["IJKab", "1D李周", ")）王E3", "@4567",
                  "45ABCD李周吴郑",
                  "i678","0xD0CF11E7A0525E3CF4E274A14D27EE5788301E0221163603E7D8B24DD79607A1C61A74E9D3A75FAE9290701CDE503F8B911ABDF16B97B25FC110BDD3661C80057C0690EE2ADF90EEA9CFA9F000300298133A21838EC450000000049454E44AE426082"]
    name = numpy.random.choice(first_name)
    return name

def Unicode3():
    first_name = [3.1415926,-1.002,4.666,55.00333,9.897]
    name = numpy.random.choice(first_name)
    return name

def Unicode4():
    first_name = ["23:59:59",":0","1:1:1","10:10:10"]
    name = numpy.random.choice(first_name)
    return name

def Unicode5():
    first_name = [1000.0901,1.22,9999.009]
    name = numpy.random.choice(first_name)
    return name


def add_data():
    # csv header
    fieldnames = ['_number', '_varchar', '_float', '_time', '_DECIMAL']
    lst = []
    # 创建字典，字典初始化
    startTime1 = datetime.datetime.now()
    for num in range(100):
        dic = {
            '_number': None,
            '_varchar': str(None),
            '_float': None,
            '_time': None,
            '_DECIMAL': None
        }
        dic['_number'] = int(Unicode1())
        dic['_varchar'] = Unicode2()
        dic['_float'] = Unicode3()
        dic['_time'] = Unicode4()
        dic['_DECIMAL'] = Unicode5()
        # csv data
        lst.append(dic)
        del dic
    else:
        with open('H:/lyz_data/DBF_data/数据库测试数据/CSV文件/a_CSV文件4_楊.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lst)
        endTime1 = datetime.datetime.now()
        print('新增完毕，耗时：', endTime1 - startTime1,'\n')
    del lst

if __name__ == '__main__':
    pass
