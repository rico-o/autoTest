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
         unit_index = data[0].index("unit")
         initials_index = data[0].index("initials")
         si_card_id_index = data[0].index("si_card_id")
         country_index = data[0].index("country")
         phone_index = data[0].index("phone")
         team_index = data[0].index("team")
         beginDate_index = data[0].index("beginDate")
         begin_date_hh_index = data[0].index("begin_date_hh")
         begin_date_mm_index = data[0].index("begin_date_mm")
         begin_date_ss_index = data[0].index("begin_date_ss")
         play_endDate_index = data[0].index("play_endDate")
         end_date_hh_index = data[0].index("end_date_hh")
         end_date_mm_index = data[0].index("end_date_mm")
         end_date_ss_index = data[0].index("end_date_ss")
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
              case.append(data[i][unit_index])
              case.append(data[i][initials_index])
              case.append(data[i][si_card_id_index])
              case.append(data[i][country_index])
              case.append(data[i][phone_index])
              case.append(data[i][team_index])
              case.append(data[i][beginDate_index])
              case.append(data[i][begin_date_hh_index])
              case.append(data[i][begin_date_mm_index])
              case.append(data[i][begin_date_ss_index])
              case.append(data[i][play_endDate_index])
              case.append(data[i][end_date_hh_index])
              case.append(data[i][end_date_mm_index])
              case.append(data[i][end_date_ss_index])
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

     # @classmethod  # 类方法
     # def setUpClass(cls):
     #      cls.player = PlayerPage()
     #      cls.player.login()
     #      cls.player.iframe1()
     #      cls.player.base_setting()
     #      cls.player.iframe0()
     #
     # @classmethod  # 类方法
     # def tearDownClass(cls):
     #      cls.player.quit_driver()

     case = Case().get_case()

     @data(*case)
     @unpack
     def test_player_add(self, username, credentials, number_book, group,unit,initials,si_card_id,country,phone,team,beginDate,begin_date_hh,begin_date_mm,begin_date_ss,play_endDate,end_date_hh,end_date_mm,end_date_ss,result):
          """添加成功"""
          self.player.login()
          self.player.iframe1()
          self.player.base_setting()
          self.player.iframe0()
          self.player.add()
          self.player.iframe2()
          # self.player.parentframe()
          # self.player.iframeauto_player()
          self.player.player_add01(username=username, credentials=credentials, number_book=number_book, group=group ,unit=unit,initials=initials,si_card_id=si_card_id,country=country,phone=phone,team=team,beginDate=beginDate,begin_date_hh=begin_date_hh,begin_date_mm=begin_date_mm,begin_date_ss=begin_date_ss,play_endDate=play_endDate,end_date_hh=end_date_hh,end_date_mm=end_date_mm,end_date_ss=end_date_ss)


if __name__ == '__main__':
      unittest.main()
