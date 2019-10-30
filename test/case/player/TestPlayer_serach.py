from test.pages.PlayerPage import *
import unittest
from test.common.Common import *

class TestPlayerDelete(unittest.TestCase):
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


    def test_player_delete(self,):

            self.player.dropdown_menu_open()
            self.player.dropdown_menu_inner()
            self.player.search()






if __name__ == '__main__':
    unittest.main()