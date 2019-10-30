
from test.pages.PlayerPage import *
from ddt import  ddt,data,unpack
import unittest
from data.ExcelUtil import Serach_ExcelUtil
class Case(object):
    def __init__(self):
      pass

    def get_case(self):
         # 获取 Excel 中的文件数据
         sheet = 'player'
         file = Serach_ExcelUtil(sheet_name=sheet)
         data = file.get_data()
         # 得到所需要数据的索引，然后根据索引获取相应顺序的数据
         username_index = data[0].index("username")
         number_book_index = data[0].index("number_book")
         device_id__index = data[0].index("device_id")
         result_index = data[0].index("result")
         data_length = data.__len__()

         all_case = []
         # 去除 header 行，和其他无用的数据
         for i in range(1, data_length):
              case = []
              case.append(data[i][username_index])
              case.append(data[i][number_book_index])
              case.append(data[i][device_id__index])
              case.append(data[i][result_index])
              all_case.append(case)
         return all_case

# class TestSerach(unittest.TestCase,PlayerPage):
#     """运动员单个条件查询测试"""
#
#     @classmethod #类方法
#     def setUpClass(cls):
#         cls.search =PlayerPage()
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.search.quit_driver()
#
#
#     def test_player_name_serach(self):
#         """运动员姓名查询"""
#         self.search.login()
#         self.search.iframe1()
#         self.search.base_setting()
#         self.search.iframe0()
#         self.search.player_name_serach('f')
#         self.search.serach()
#
#
#     def test_player_number_book_serach(self):
#         """运动员号码簿查询"""
#         self.search.serach_clear()
#         self.search.player_number_book_serach('683')
#         self.search.serach()
@ddt
class TestSearch(unittest.TestCase):
    """运动员按条件查询测试"""
    @classmethod  # 类方法
    def setUpClass(cls):
        cls.search = PlayerPage()
        cls.search.login()
        cls.search.iframe1()
        cls.search.base_setting()
        cls.search.iframe0()

    @classmethod  # 类方法
    def tearDownClass(cls):
        cls.search.quit_driver()

    case = Case().get_case()

    @data(*case)
    @unpack
    def test_player_search(self, username, number_book,device_id,result):
          """按条件查询测试"""
          self.search.player_search(username=username, number_book=number_book, device_id=device_id)
          self.search.search()
          time.sleep(3)
          self.search.search_clear()






if __name__ == '__main__':
    unittest.main()

