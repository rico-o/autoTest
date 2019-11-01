from test.pages.SettingPage import *
import unittest
class Test_Setting_map_marker(unittest.TestCase):
    """路线绘制—查看地图测试"""

    @classmethod #类方法
    def setUpClass(cls):
        cls.setting = SettingPage()
        cls.setting.login()
        cls.setting.iframe1()
        cls.setting.base_setting()
        cls.setting.iframe01()
        cls.setting.setting()
        cls.setting.iframe0()


    def test_map_marker(self):
        self.setting.map_draw()
        self.setting.iframe3()
        self.setting.map_marker()

    @classmethod
    def tearDownClass(cls):
        cls.setting.quit_driver()
