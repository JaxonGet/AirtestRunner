# -*- coding: utf-8 -*-
# Created by iFantastic on 2018/12/23
"""

author: jaxon
create time: 2018/12/23

"""
import time
import os


T = int(time.time())
'''当前文件所在目录的父目录的绝对路径'''
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 用例目录
test_suite_dir = parentDirPath + r'/Common'
# 报告目录
Report_dir = parentDirPath + r'/TestReport/'
Broker_APP_name = "com.huifenqi.broker"

global Contract_no

if __name__ == '__main__':
    try:
        print('213')
    except:
        print("444")