import unittest
from test.pages.PlayerPage import *
from data.ExcelUtil import *
from ddt import  ddt,data,unpack

class Case(object):
    def __init__(self):
      pass

    def get_case(self):
         # 获取 Excel 中的文件数据
         sheet = 'player'
         file = ExcelUtil(sheet_name=sheet)
         data = file.get_data()
         # 得到所需要数据的索引，然后根据索引获取相应顺序的数据
         username_index = data[0].index("username")
         credentials_index = data[0].index("credentials")
         number_book_index = data[0].index("number_book")
         group_index = data[0].index("group")
         beginDate_index = data[0].index("beginDate")
         result_index = data[0].index("result")
         data_length = data.__len__()

         all_case = []
         # 去除 header 行，和其他无用的数据
         for i in range(1, data_length):
              case = []
              case.append(data[i][username_index])
              case.append(data[i][credentials_index])
              case.append(data[i][number_book_index])
              case.append(data[i][group_index])
              case.append(data[i][beginDate_index])
              case.append(data[i][result_index])
              all_case.append(case)
         return all_case
@ddt
class TestPlayerAdd(unittest.TestCase):
     """运动员添加测试"""
     def setUp(self):
         self.player = PlayerPage()

     def tearDown(self):
         self.player.quit_driver()

     case = Case().get_case()

     @data(*case)
     @unpack
     def test_player_add(self, username, credentials,number_book,group, beginDate,result):
          """添加成功"""
          self.player.login()
          self.player.iframe1()
          self.player.base_setting()
          self.player.iframe0()
          self.player.add()
          self.player.iframe2()
          self.player.player_add01(username=username, credentials=credentials, number_book=number_book, group=group ,beginDate=beginDate)


if __name__ == '__main__':
      unittest.main()
