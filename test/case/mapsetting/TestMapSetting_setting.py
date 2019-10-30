import unittest
from test.pages.MapSettingPage import *

class Test_setting(unittest.TestCase):
    """设置"""
    @classmethod  # 类方法
    def setUpClass(cls):
        cls.setting = MapSettingPage()


    def test_setting(self):
        self.setting.login()
        self.setting.iframe1()
        self.setting.base_setting()
        self.setting.iframe01()
        self.setting.map_setting()
        self.setting.iframe00()
        self.setting.setting()
        self.setting.parentframe()
        self.setting.iframe3()
        self.setting.defalut_coordinates_add()
        self.setting.parentframe()
        self.setting.setting_error()


    @classmethod
    def tearDownClass(cls):
        cls.setting.quit_driver()
