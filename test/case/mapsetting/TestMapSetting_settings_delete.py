import unittest
from test.pages.MapSettingPage import *

class Test_settings_delete(unittest.TestCase):
    """批量删除地图"""
    @classmethod  # 类方法
    def setUpClass(cls):
        cls.setting = MapSettingPage()


    def test_settings_delete(self):
        self.setting.login()
        self.setting.iframe1()
        self.setting.base_setting()
        self.setting.iframe01()
        self.setting.map_setting()
        self.setting.iframe00()
        self.setting.select()
        self.setting.delete()
        self.setting.delete_confirm()


    @classmethod
    def tearDownClass(cls):
        cls.setting.quit_driver()
