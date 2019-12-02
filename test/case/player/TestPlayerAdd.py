# coding=utf-8  

import unittest
from test.pages.PlayerPage import PlayerPage
from time import sleep

class TestPlayerAdd(unittest.TestCase):
    """运动员日期选择器测试"""

    @classmethod #类方法
    def setUpClass(cls):
        cls.player = PlayerPage()

    @classmethod
    def tearDownClass(cls):
        cls.player.quit_driver()

    def test_add01(self):
        """添加成功"""
        self.player.login()
        self.player.iframe1()
        self.player.base_setting()
        self.player.iframe0()
        self.player.add()
        self.player.iframe2()
        self.player.player_add('player01','440','020','group01','1111','1111','1111','1111','1111')
        self.player.datetimepicker()
        self.player.save()



if __name__ == '__main__':

    unittest.main()
