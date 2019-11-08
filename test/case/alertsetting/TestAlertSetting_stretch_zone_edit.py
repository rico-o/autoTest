from test.pages.AlertPage import *
import unittest
class Test_Setting_track_edit(unittest.TestCase):
    """超速报警——编辑测试"""

    @classmethod #类方法
    def setUpClass(cls):
        cls.setting = AlertPage()
        cls.setting.login()
        cls.setting.iframe1()
        cls.setting.base_setting()
        cls.setting.iframe01()
        cls.setting.alter_setting()
        cls.setting.iframe0()


    def test_track_edit(self):
        self.setting.stretch_zone()
        self.setting.iframe3()
        self.setting.track_edit()
        self.setting.iframe4()
        self.setting.track_speed()
        self.setting.save()


    @classmethod
    def tearDownClass(cls):
        cls.setting.quit_driver()