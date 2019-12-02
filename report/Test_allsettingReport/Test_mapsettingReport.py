# coding=utf-8
from HTMLTestRunner import HTMLTestRunner

from test.case.mapsetting.TestMapSetting_add_coordinates import *
from test.case.mapsetting.TestMapSetting_add_map import *
from test.case.mapsetting.TestMapSetting_setting import *
from test.case.mapsetting.TestMapSetting_settings import *
from test.case.mapsetting.TestMapSetting_live_setting_img import *
from test.case.mapsetting.TestMapSetting_settings_delete import *
from test.case.mapsetting.TestMapSetting_live_setting_sign import *
from test.case.mapsetting.TestMapSetting_adjustmap import *
from test.case.mapsetting.TestMapSetting_adjustmap_param import *
from test.case.mapsetting.TestMapSetting_check_map import *
import time
if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Test_add_coordinates('test_defalut_coordinates'))
    testunit.addTest(Test_add_map('test_map'))
    testunit.addTest(Test_check_map('test_check_map'))
    testunit.addTest(Test_setting('test_setting'))
    testunit.addTest(Test_settings('test_settings'))
    testunit.addTest(Test_live_setting_img('test_live_setting_img'))
    testunit.addTest(Test_live_setting_sign('test_live_setting_sign'))
    testunit.addTest(Test_settings_delete('test_settings_delete'))
    testunit.addTest(Test_adjustmap('test_adjustmap'))
    testunit.addTest(Test_adjustmap_param('test_map_param'))
    testunit.addTest(Test_check_map('test_check_map'))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = 'F:/location/产品测试/自动化测试/测试报告/' + now + '地图设置自动化.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title="地图设置测试",
        description="地图设置分步骤测试")
    runner.run(testunit)
