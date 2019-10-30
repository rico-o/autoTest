import os, time, unittest
import HTMLTestRunner
# 获取当前时间
now = time.strftime('%Y-%m-%d %H_%M_%S')
# 标题
title = "测试报告"
# 设置报告存放路径，并且以当前时间进行报告命名。
filename = 'F:/location/产品测试/自动化测试/测试报告/' + now + ' Testreport.html'
def all_case():
# 导入所有的用例"""
   case_path = os.getcwd()
   discover = unittest.defaultTestLoader.discover(case_path,pattern="Test*.py")
   print(discover)
   return discover

if __name__ == "__main__":
 fp = open(filename, "wb")
 runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=title)
 runner.run(all_case())
 fp.close()
