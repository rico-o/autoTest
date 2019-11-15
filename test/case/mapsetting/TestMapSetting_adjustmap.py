import unittest
from test.pages.MapSettingPage import *

class Test_adjustmap(unittest.TestCase):
    """校准——点取"""
    @classmethod  # 类方法
    def setUpClass(cls):
        cls.setting = MapSettingPage()


    def test_adjustmap(self):
        self.setting.login()
        self.setting.iframe1()
        self.setting.base_setting()
        self.setting.iframe01()
        self.setting.map_setting()
        self.setting.iframe00()
        self.setting.adjustmap()
        self.setting.iframe3()
        self.setting.left_choose()
        self.setting.right_choose()
        self.setting.adjustmap_second()
        self.setting.iframe4()
        self.setting.save()

    @classmethod
    def tearDownClass(cls):
        cls.setting.quit_driver()
