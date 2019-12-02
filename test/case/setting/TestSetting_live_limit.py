from test.pages.SettingPage import *
import unittest
class Test_Setting_live_limit(unittest.TestCase):
    """直播限制—统一开放时间测试"""

    @classmethod #类方法
    def setUpClass(cls):
        cls.setting = SettingPage()
        cls.setting.login()
        cls.setting.iframe1()
        cls.setting.base_setting()
        cls.setting.iframe01()
        cls.setting.setting()
        cls.setting.iframe0()


    def test_live_limit(self):
        self.setting.live_limit()
        self.setting.iframe3()
        self.setting.begin_date()
        self.setting.begin_date_hh()
        self.setting.begin_date_mm()
        self.setting.begin_date_ss()

    @classmethod
    def tearDownClass(cls):
        cls.setting.quit_driver()
