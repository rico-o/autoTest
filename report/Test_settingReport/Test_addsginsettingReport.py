# # coding=utf-8
# from HTMLTestRunner import HTMLTestRunner
# from test.case.signsetting.TestSignSetting_add import *
# from test.case.signsetting.TestSignSetting_edit import *
# import time
# if __name__ == '__main__':
#     testunit = unittest.TestSuite()
#     testunit.addTest(Test_Sign_Setting_add('test_add'))
#     testunit.addTest(Test_Sign_Setting_edit('test_edit'))
#     now = time.strftime('%Y-%m-%d %H_%M_%S')
#     filename = 'F:/location/产品测试/自动化测试/测试报告/' + now + '签到点管理自动化.html'
#     fp = open(filename, 'wb')
#     runner = HTMLTestRunner(
#         stream=fp,
#         title="签到点管理设置测试",
#         description="签到点管理设置分步骤测试")
#     runner.run(testunit)
