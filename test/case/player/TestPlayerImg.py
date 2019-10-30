from test.pages.PlayerPage import *
import unittest


class TestPlayerImg(unittest.TestCase):
    """运动员图片设置"""
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

    def test_player_img_add(self):
        self.player.img()
        self.player.iframe2()
        self.player.add_imgs()



if __name__ == '__main__':
    unittest.main()