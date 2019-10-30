
import unittest
from HTMLTestRunner import HTMLTestRunner
from test.case.player.TestPlayerImgs import *
from test.case.player.TestPlayerImg import *
import time

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(TestPlayerImg('test_player_img_add'))
    testunit.addTest(TestPlayerImgs('test_player_img_adds'))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = 'F:/location/产品测试/自动化测试/测试报告/' + now + 'test_player_img_add.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title="运动员图片批量修改测试",
        description="运动员图片修改自动化测试")
    runner.run(testunit)