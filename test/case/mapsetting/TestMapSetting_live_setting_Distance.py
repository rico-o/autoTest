from test.pages.MapSettingPage import *
import unittest

class Test_live_setting_addDistance(unittest.TestCase):
    """直播签到点图片设置"""
    @classmethod  # 类方法

    def setUp(self):
      self.setting = MapSettingPage()

    def test_live_setting_addDistance(self):
        self.setting.login()
        self.setting.iframe1()
        self.setting.base_setting()
        self.setting.iframe01()
        self.setting.map_setting()
        self.setting.iframe00()
        self.setting.live_setting()
        self.setting.parentframe()
        self.setting.iframe3()
        self.setting.addDistance()
        self.setting.iframe4()
        self.setting.addDistance_name()
        self.setting.submit()


    def tearDown(self):
        self.setting.quit_driver()

