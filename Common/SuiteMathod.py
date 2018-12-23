# -*- coding: utf-8 -*-
# Created by iFantastic on 2018/12/23
"""

author: jaxon
create time: 2018/12/23

"""

import unittest
import HTMLTestRunner
import time
from Config.VarConfig import *


def creatsuite():
    testunit = unittest.TestSuite()
    # 定义测试文件查找的目录
    test_dir = test_suite_dir
    package_tests = unittest.defaultTestLoader.discover(test_dir,
                                                        pattern='Test*.py',
                                                        top_level_dir=None)
    # 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in package_tests:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit


alltestnames = creatsuite()

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    test_report = Report_dir
    filename = test_report + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'UI自动化测试报告',
        description=u'测试用例执行结果'
    )

    runner.run(alltestnames)