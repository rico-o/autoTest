from test.pages.MapSettingPage import *
import unittest

class Test_live_setting_distance_add(unittest.TestCase):
    """直播设置--添加路程对比"""
    @classmethod  # 类方法

    def setUp(self):
      self.setting = MapSettingPage()

    def test_live_setting_distance_add(self):
        self.setting.login()
        self.setting.iframe1()
        self.setting.base_setting()
        self.setting.iframe01()
        self.setting.map_setting()
        self.setting.iframe00()
        self.setting.live_setting()
        self.setting.parentframe()
        self.setting.iframe3()
        self.setting.distance_button()
        self.setting.iframe4()
        self.setting.distance_select_track_button()
        self.setting.iframe5()
        self.setting.distance_select_track()


    def tearDown(self):
        self.setting.quit_driver()
