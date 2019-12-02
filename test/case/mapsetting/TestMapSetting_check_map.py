import unittest
from test.pages.MapSettingPage import *

class Test_check_map(unittest.TestCase):
    """查看图片"""
    @classmethod  # 类方法
    def setUpClass(cls):
        cls.setting = MapSettingPage()


    def test_check_map(self):
        self.setting.login()
        self.setting.iframe1()
        self.setting.base_setting()
        self.setting.iframe01()
        self.setting.map_setting()
        self.setting.iframe00()
        self.setting.check_map()





    @classmethod
    def tearDownClass(cls):
        cls.setting.quit_driver()
