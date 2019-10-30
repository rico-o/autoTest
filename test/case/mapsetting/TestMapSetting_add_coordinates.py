import unittest
from test.pages.MapSettingPage import *

class Test_add_coordinates(unittest.TestCase):
    """默认坐标测试"""

    @classmethod  # 类方法
    def setUpClass(cls):
     cls.setting = MapSettingPage()


    def test_defalut_coordinates(self):
        self.setting.login()
        self.setting.iframe1()
        self.setting.base_setting()
        self.setting.iframe01()
        self.setting.map_setting()
        self.setting.iframe00()
        self.setting.defalut_coordinates()
        self.setting.parentframe()
        self.setting.iframe3()
        self.setting.defalut_coordinates_add()
        try:
            self.setting.parentframe()
            self.setting.close_button()
        except:
            print("请保证默认坐标的左上角和右下角坐标有填或者不填")

    @classmethod
    def tearDownClass(cls):
        cls.setting.quit_driver()
