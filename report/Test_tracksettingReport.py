# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from test.case.tracksetting.TestTrackSetting_gpx_delete import *
from test.case.tracksetting.TestTrackSetting_gpx import *
from test.case.tracksetting.TestTrackSetting_gpx_serach import *
import time
if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Test_Track_Setting_gpx('test_gpx'))
    testunit.addTest(Test_Track_Setting_gpx_search('test_gpx_search'))
    testunit.addTest(Test_Track_Setting_gpx_delete('test_gpx_delete'))

    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = 'F:/location/产品测试/自动化测试/测试报告/' + now + '轨迹管理自动化.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title="轨迹管理测试",
        description="轨迹管理分步骤测试")
    runner.run(testunit)

