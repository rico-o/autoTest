# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from test.case.alertsetting.TestAlertSetting_sos_phone import *
from test.case.alertsetting.TestAlertSetting_stretch_zone import *
from test.case.alertsetting.TestAlertSetting_stretch_zone_delete import *
from test.case.alertsetting.TestAlertSetting_stretch_zone_edit import *
from test.case.alertsetting.TestAlertSetting_time_out import *
from test.case.alertsetting.TestAlertSetting_time_out_close import *
import time
if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Test_Setting_phone('test_exception_phone'))
    testunit.addTest(Test_Setting_select_track('test_select_track'))
    testunit.addTest(Test_Setting_track_edit('test_track_edit'))
    testunit.addTest(Test_Setting_track_delete('test_track_delete'))
    testunit.addTest(Test_Setting_time_out_setting('test_select_track'))
    testunit.addTest(Test_Setting_time_out_setting_close('test_time_out_delete'))

    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = 'F:/location/产品测试/自动化测试/测试报告/' + now + '报警设置自动化.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title="报警测试",
        description="报警分步骤测试")
    runner.run(testunit)
