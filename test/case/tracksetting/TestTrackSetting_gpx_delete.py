from test.pages.TrackSettingPage import *
import unittest
class Test_Track_Setting_gpx_delete(unittest.TestCase):
    """轨迹管理——删除gpx测试"""

    @classmethod #类方法
    def setUpClass(cls):
        cls.setting = TrackSettingPage()
        cls.setting.login()
        cls.setting.iframe1()
        cls.setting.base_setting()
        cls.setting.iframe01()
        cls.setting. track_setting()
        cls.setting.iframe0()


    def test_gpx_delete(self):
        self.setting.track_delete()
        self.setting.parentframe()
        self.setting.delete_confirm()

    @classmethod
    def tearDownClass(cls):
        cls.setting.quit_driver()