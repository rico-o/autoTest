from test.pages.AlertPage import *
import unittest
class Test_Setting_area_edit(unittest.TestCase):
    """围栏设置——编辑测试"""

    @classmethod #类方法
    def setUpClass(cls):
        cls.setting = AlertPage()
        cls.setting.login()
        cls.setting.iframe1()
        cls.setting.base_setting()
        cls.setting.iframe01()
        cls.setting.alter_setting()
        cls.setting.iframe0()


    def test_edit_area(self):
        self.setting.enclosure_area()
        self.setting.iframe3()
        self.setting.area_edit()
        self.setting.save_chain()



    @classmethod
    def tearDownClass(cls):
        cls.setting.quit_driver()