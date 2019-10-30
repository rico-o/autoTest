import unittest
from test.pages.MapSettingPage import *

class Test_add_map(unittest.TestCase):
    """上传图片和底图"""
    @classmethod  # 类方法
    def setUpClass(cls):
        cls.setting = MapSettingPage()


    def test_map(self):
        self.setting.login()
        self.setting.iframe1()
        self.setting.base_setting()
        self.setting.iframe01()
        self.setting.map_setting()
        self.setting.iframe00()
        self.setting.add_map()
        self.setting.live_map()
        self.setting.parentframe()
        self.setting.iframe3()
        self.setting.upload_img()


    @classmethod
    def tearDownClass(cls):
        cls.setting.quit_driver()
