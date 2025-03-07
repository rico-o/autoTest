from test.pages.SettingPage import *
import unittest
class Test_Setting_select_track(unittest.TestCase):
    """路线绘制测试"""

    @classmethod #类方法
    def setUpClass(cls):
        cls.setting = SettingPage()
        cls.setting.login()
        cls.setting.iframe1()
        cls.setting.base_setting()
        cls.setting.iframe01()
        cls.setting.setting()
        cls.setting.iframe0()


    def test_select_track(self):
        self.setting.map_draw()
        self.setting.iframe3()
        self.setting.select_track()
        self.setting.iframe4()
        self.setting.select_all()
        self.setting.confirm()


    @classmethod
    def tearDownClass(cls):
        cls.setting.quit_driver()
