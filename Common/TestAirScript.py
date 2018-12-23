# -*- coding: utf-8 -*-
# Created by iFantastic on 2018/12/23
"""

author: jaxon
create time: 2018/12/23

"""
from TestCase.Test_FQ import *
import unittest


class AirScript(unittest.TestCase):

    # def setUpClass(self):
    #     # 连接设备
    #     connect_device('Android:///')

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


    def test_CreateContract(self):
        try:
            assert_equal(CreateContract(), "请租客在72小时内扫描二维码完善并确认")
            print('执行成功')
        except:
            print('执行失败')

if __name__ == '__main__':
    unittest.main()