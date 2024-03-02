# -*- coding:utf-8 -*-
"""
@Time        : 2023/11/24
@File        : report.py
@Author      : lyz
@version     : python 3
@Description :
"""
from datetime import datetime
from PyUtilToolKit.pathSetting import ensure_path
import xml.etree.ElementTree as eT

class TestReportWrapper:
    def __init__(self):
        self.total = 0
        self.error = 0
        self.passed = 0
        self.failed = 0
        self.elapsed_time = 0
        self.skipped = 0
        self.times = 0
    def get_summary(self):
        # 解析测试结果xml文件
        tree = eT.parse(ensure_path("\\yiXie_9_report\\result.xml"))
        tree_getroot = tree.getroot()
        result_json = dict(tree_getroot.find("testsuite").items())
        # 通过数、结束时间、总数
        self.total = int(result_json["tests"])
        self.passed = (int(result_json["tests"]) - int(result_json["failures"]))
        self.times = (datetime.strptime(result_json["timestamp"],
                                        "%Y-%m-%dT%H:%M:%S.%f")).strftime("%Y-%m-%d %H:%M:%S")
        # 计算通过率
        pass_rate = self.passed / self.total * 100 if self.total > 0 else 0
        # 返回通过数、总数、失败数、错误、耗时、跳过和统计结果
        summary = {
            "total": self.total,
            "passed": self.passed,
            "failed": result_json["failures"],
            "errors": result_json["errors"],
            "skipped": result_json["skipped"],
            "pass_rate": round(pass_rate, 2),
            "timestamp": self.times,
            "elapsed_time": result_json["time"]
        }
        return summary
    def custom_statistics(self):
        # 添加其他自定义统计功能
        pass

if __name__ == '__main__':
    # a = time.time()
    # print(os.path.exists(ensure_path("\\yiXie_9_report\\report.html")))
    print(TestReportWrapper().get_summary())
