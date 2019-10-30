# coding=utf-8  

import unittest
from test.pages.PlayerPage import PlayerPage
from time import sleep

class TestPlayAdd(unittest.TestCase):
    """登录测试"""

    @classmethod #类方法
    def setUpClass(cls):
        cls.player = PlayerPage()

    @classmethod
    def tearDownClass(cls):
        cls.player.quit_driver()

    def test_add01(self):
        """添加成功"""
        self.player.login()
        # sleep(3)
        # self.player.player_add()
        self.player.iframe1()
        self.player.base_setting()
        self.player.iframe0()
        self.player.add()
        sleep(3)
        self.player.iframeauto()
        sleep(3)
        self.player.player_add('player01','440','020','group01','2019-09-20')
        sleep(3)


if __name__ == '__main__':

    unittest.main()
