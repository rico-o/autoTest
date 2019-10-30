import unittest
from test.pages.WorkerPage import *
from data.ExcelUtil import *
from ddt import  ddt,data,unpack

class Case(object):

    def __init__(self):
      pass

    def get_case(self):
         # 获取 workrer Excel 中的文件数据
         sheet = 'worker'
         file = Worker_ExcelUtil(sheet_name=sheet)
         data = file.get_data()
         # 得到所需要数据的索引，然后根据索引获取相应顺序的数据
         worker_name_index = data[0].index("worker_name")
         device_id_index = data[0].index("device_id")
         result_index = data[0].index("result")
         data_length = data.__len__()

         all_case = []
         # 去除 header 行，和其他无用的数据
         for i in range(1, data_length):
              case = []
              case.append(data[i][worker_name_index])
              case.append(data[i][device_id_index])
              case.append(data[i][result_index])
              all_case.append(case)
         return all_case
@ddt
class TestWorkerAdd(unittest.TestCase):
     """工作人员添加测试"""


     def setUp(self):
         self.worker = WorkerPage()
         self.worker.login()
         self.worker.iframe1()
         self.worker.base_setting()
         self.worker.iframe01()
         self.worker.worker()
         self.worker.iframe0()


     def tearDown(self):
         self.worker.quit_driver()

     case = Case().get_case()

     @data(*case)
     @unpack
     def test_worker_add(self,worker_name,device_id,result):
         """添加成功"""
         self.worker.add_button()
         self.worker.parentframe()
         self.worker.iframe3()
         self.worker.worker_add01(worker_name=worker_name,device_id=device_id)
         # self.worker.parentframe()
         # self.worker.iframe00()



if __name__ == '__main__':
      unittest.main()