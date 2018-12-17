import unittest
import HTMLTestRunner

# import smtplib
#####from email.mime.text import MIMEText
from email.header import Header
import time
import os
from tomorrow import threads  #多线程
from BeautifulReport import BeautifulReport  #测试结果


# 获取路径
curpath = os.path.dirname(os.path.realpath(__file__))
casepath = os.path.join(curpath, "mail", "test_case") #拼接路径
reportpath = os.path.join(curpath, "mail", "report")


def add_case(case_path=casepath):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern='login_case.py',
                                                  top_level_dir=None)
    return discover

@threads(4)
def run(test_suit, report_path=reportpath):
    result = BeautifulReport(test_suit)
    result.report(filename='report.html', description='测试报告', log_path=report_path)
#filename='report.html'文件名称，log_path=report_path 测试结果保存路径

if __name__ == "__main__":
    # 用例集合
    cases = add_case()
    for i in cases:
        run(i)



