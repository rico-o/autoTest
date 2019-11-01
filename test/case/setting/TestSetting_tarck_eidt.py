from test.pages.SettingPage import *
import unittest
class Test_Setting_track_edit(unittest.TestCase):
    """路线绘制——编辑测试"""

    @classmethod #类方法
    def setUpClass(cls):
        cls.setting = SettingPage()
        cls.setting.login()
        cls.setting.iframe1()
        cls.setting.base_setting()
        cls.setting.iframe01()
        cls.setting.setting()
        cls.setting.iframe0()


    def test_track_edit(self):
        self.setting.map_draw()
        self.setting.iframe3()
        self.setting.track_edit()
        self.setting.iframe4()
        self.setting.edit_color()
        self.setting.save()


    @classmethod
    def tearDownClass(cls):
        cls.setting.quit_driver()
