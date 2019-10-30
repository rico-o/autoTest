from test.pages.PlayerPage import *
import unittest


class TestPlayerEdit(unittest.TestCase):
    """运动员编辑"""
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

    def test_player_import(self):
        """运动员编辑"""
        self.player.edit()
        self.player.iframe2()
        self.player.player_edit('player01','440','020','group01')



if __name__ == '__main__':
    unittest.main()