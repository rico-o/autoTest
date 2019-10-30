from test.pages.PlayerPage import *
import unittest

class TestDeviceImport(unittest.TestCase):
    """运动员批量发放设备"""
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
          self.player.provide_device()
          # self.player.parentframe()
          self.player.iframe2()
          self.player.import_device()
          self.player.UpLoad_File('F:\location\产品测试\自动化测试\\autoTest\data\副本批量发放模板2019-09-26.xlsx')
          self.player.parentframe()
          try:
              self.player.error_message_device()
          except:
              print('导入成功')


if __name__ == '__main__':
    unittest.main()