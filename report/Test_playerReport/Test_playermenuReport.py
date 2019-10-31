from HTMLTestRunner import HTMLTestRunner

from test.case.player.TestPlayer_serach import *
from test.case.player.TestPlayer_serach_unit import *
from test.case.player.TestPlayer_serach_contry import *


import time
if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(TestPlayer_serach('test_player_group_serach'))
    testunit.addTest(TestPlayer_unit_serach('test_player_unit_serach'))
    testunit.addTest(TestPlayer_country_serach('test_player_country_serach'))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = 'F:/location/产品测试/自动化测试/测试报告/' + now + '工作人员自动化.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title="工作人员下拉菜单测试",
        description="工作人员下拉菜单测试",
        )
    runner.run(testunit)
