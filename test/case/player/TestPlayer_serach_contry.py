from test.pages.PlayerPage import *
import unittest
from test.common.Common import *

class TestPlayer_country_serach(unittest.TestCase):
    """运动员下拉列表查询"""
    @classmethod  # 类方法
    def setUpClass(cls):
        cls.player = PlayerPage()
        cls.player.login()
        cls.player.iframe1()
        cls.player.base_setting()
        cls.player.iframe0()

    @classmethod  # 类方法
    def tearDownClass(cls):
        cls.player.quit_driver()

    def test_player_country_serach(self, ):
        self.player.country_menu()
