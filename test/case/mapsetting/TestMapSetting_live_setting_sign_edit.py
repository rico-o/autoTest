import unittest
from test.pages.MapSettingPage import *

class Test_live_setting_sign_edit(unittest.TestCase):
    """直播签到点编辑"""
    @classmethod  # 类方法

    def setUp(self):
      self.setting = MapSettingPage()

    def test_live_setting_sign_edit(self):
        self.setting.login()
        self.setting.iframe1()
        self.setting.base_setting()
        self.setting.iframe01()
        self.setting.map_setting()
        self.setting.iframe00()
        self.setting.live_setting()
        self.setting.iframe3()
        self.setting.sign_edit()
        self.setting.iframe4()
        self.setting.sign('自动点','30')


    def tearDown(self):
        self.setting.quit_driver()

