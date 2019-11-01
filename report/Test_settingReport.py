# coding=utf-8
from HTMLTestRunner import HTMLTestRunner

from test.case.mapsetting.TestMapSetting_add_coordinates import *
from test.case.mapsetting.TestMapSetting_add_map import *
from test.case.setting.TestSetting_sos_phone import *
from test.case.mapsetting.TestMapSetting_setting import *
from test.case.mapsetting.TestMapSetting_settings import *
from test.case.mapsetting.TestMapSetting_live_setting_img import *
from test.case.mapsetting.TestMapSetting_settings_delete import *
from test.case.mapsetting.TestMapSetting_live_setting_sign import *
from test.case.setting.TestSetting_mapdraw import *
from test.case.setting.TestSetting_map_marker import *
from test.case.setting.TestSetting_tarck_delete import *
from test.case.setting.TestSetting_tarck_eidt import *
from test.case.setting.TestSetting_tarck_view import *
import time
if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Test_Setting_phone('test_exception_phone'))
    testunit.addTest(Test_Setting_select_track('test_select_track'))
    testunit.addTest(Test_Setting_map_marker('test_map_marker'))
    testunit.addTest(Test_Setting_track_edit('test_track_edit'))
    testunit.addTest(Test_Setting_track_delete('test_track_delete'))
    testunit.addTest(Test_Setting_track_view('test_track_view'))
    testunit.addTest(Test_add_coordinates('test_defalut_coordinates'))
    testunit.addTest(Test_add_map('test_map'))
    testunit.addTest(Test_setting('test_setting'))
    testunit.addTest(Test_settings('test_settings'))
    testunit.addTest(Test_live_setting_img('test_live_setting_img'))
    testunit.addTest(Test_live_setting_sign('test_live_setting_sign'))
    testunit.addTest(Test_settings_delete('test_settings_delete'))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = 'F:/location/产品测试/自动化测试/测试报告/' + now + '设置和地图设置自动化.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title="设置和地图设置测试",
        description="设置分步骤测试")
    runner.run(testunit)
