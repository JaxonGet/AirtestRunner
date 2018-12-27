# -*- coding: utf-8 -*-
# Created by iFantastic on 2018/12/23
"""

author: jaxon
create time: 2018/12/23

"""
from TestCase.Test_FQ import *
import unittest


class AirScript(unittest.TestCase):


    def setUp(self):
        print('')
        print('------开始执行------')
        # 连接设备
        connect_device('Android:///')
        # 清理APP缓存
        clear_app(Broker_APP_name)
        # 启动APP
        start_app(Broker_APP_name)

    def tearDown(self):
        print('------执行完毕------')
        # 清理APP缓存
        clear_app(Broker_APP_name)

    def test_login(self):
        # 登录
        self.assertEqual(Login(), "以后再说")


    def test_SetRentInfo(self):
        # 填写租住信息
        self.assertEqual(SetRentInfo(), True)


    def test_SetInstallment(self):
        # 填写分期信息
        self.assertEqual(SetInstallment(), True)


    def test_CreateContract(self):
        # 创建分期合同
        self.assertEqual(CreateContract(), "请租客在72小时内扫描二维码完善并确认")
        # print("合同号为12：", Contract_no)




if __name__ == '__main__':
    unittest.main()
