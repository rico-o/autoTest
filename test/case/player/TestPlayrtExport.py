from test.pages.PlayerPage import *
import unittest

class TestPlayerExport(unittest.TestCase):
    """运动员导出"""
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

    def test_player_export(self):
          """运动员导入和发放"""
          self.player.export_player()



if __name__ == '__main__':
    unittest.main()