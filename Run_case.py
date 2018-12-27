# -*- coding: utf-8 -*-
# Created by iFantastic on 2018/12/23
"""

author: jaxon
create time: 2018/12/23

"""

import HTMLTestRunner
from Config.VarConfig import *
from Common.SuiteMathod import creatsuite

alltestnames = creatsuite()
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

if __name__ == '__main__':
    runner.run(alltestnames)