from test.pages.PlayerPage import *
import unittest
from test.common.Common import *

class TestPlayerImgs_delete(unittest.TestCase):
    """运动员图片批量删除"""
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

    def test_player_imgs_delete(self):
        self.player.player_select()
        self.player.delete_img()
        self.player.parentframe()
        self.player.delete_confirm()


if __name__ == '__main__':
    unittest.main()