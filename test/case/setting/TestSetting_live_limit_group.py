from test.pages.SettingPage import *
import unittest
class TestSetting_live_limit_group(unittest.TestCase):
    """直播限制—每个参赛组别开放时间测试"""

    @classmethod #类方法
    def setUpClass(cls):
        cls.setting = SettingPage()
        cls.setting.login()
        cls.setting.iframe1()
        cls.setting.base_setting()
        cls.setting.iframe01()
        cls.setting.setting()
        cls.setting.iframe0()


    def test_live_limit_group(self):
        self.setting.live_limit()
        self.setting.iframe3()
        self.setting.live_limit_group()
        self.setting.group_time()
        self.setting.submit_form()

    @classmethod
    def tearDownClass(cls):
        cls.setting.quit_driver()
