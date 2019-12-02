# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from test.case.setting.TestSetting_mapdraw import *
from test.case.setting.TestSetting_map_marker import *
from test.case.setting.TestSetting_tarck_delete import *
from test.case.setting.TestSetting_tarck_eidt import *
from test.case.setting.TestSetting_tarck_view import *
from test.case.setting.TestSetting_live_limit import *
from test.case.setting.TestSetting_live_limit_group import *
import time
if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Test_Setting_select_track('test_select_track'))
    testunit.addTest(Test_Setting_map_marker('test_map_marker'))
    testunit.addTest(Test_Setting_track_edit('test_track_edit'))
    testunit.addTest(Test_Setting_track_delete('test_track_delete'))
    testunit.addTest(Test_Setting_track_view('test_track_view'))
    testunit.addTest(Test_Setting_live_limit('test_live_limit'))
    testunit.addTest(TestSetting_live_limit_group('test_live_limit_group'))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = 'F:/location/产品测试/自动化测试/测试报告/' + now + '设置自动化.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title="设置测试",
        description="设置分步骤测试")
    runner.run(testunit)
