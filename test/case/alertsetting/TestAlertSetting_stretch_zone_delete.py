from test.pages.AlertPage import *
import unittest
class Test_Setting_track_delete(unittest.TestCase):
    """超速报警——删除测试"""

    @classmethod #类方法
    def setUpClass(cls):
        cls.setting = AlertPage()
        cls.setting.login()
        cls.setting.iframe1()
        cls.setting.base_setting()
        cls.setting.iframe01()
        cls.setting.alter_setting()
        cls.setting.iframe0()


    def test_track_delete(self):
        self.setting.stretch_zone()
        self.setting.iframe3()
        self.setting.track_delete()
        self.setting.parentframe()
        self.setting.delete_confirm()

    @classmethod
    def tearDownClass(cls):
        cls.setting.quit_driver()