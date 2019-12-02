from test.pages.PlayerPage import *
import unittest
from test.common.Common import *

class TestPlayerImport(unittest.TestCase):
    """运动员导入"""
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
          """运动员导入和发放"""
          self.player.import_player()
          self.player.UpLoad_File('F:\location\产品测试\自动化测试\\autoTest\data\duorenceshi.xlsx')
          self.player.parentframe()
          try:
            self.player.error_message_import()
          except:
              print('导入成功')



if __name__ == '__main__':
    unittest.main()