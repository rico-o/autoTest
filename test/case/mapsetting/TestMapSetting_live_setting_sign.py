import unittest
from test.pages.MapSettingPage import *

class Test_live_setting_sign(unittest.TestCase):
    """直播签到点设置"""
    @classmethod  # 类方法

    def setUp(self):
      self.setting = MapSettingPage()

    def test_live_setting_sign(self):
        self.setting.login()
        self.setting.iframe1()
        self.setting.base_setting()
        self.setting.iframe01()
        self.setting.map_setting()
        self.setting.iframe00()
        self.setting.live_setting()
        self.setting.iframe3()
        self.setting.addSign()
        self.setting.iframe4()
        self.setting.addsign('111', '23.147796,113.277602', '10')

    def tearDown(self):
        self.setting.quit_driver()

