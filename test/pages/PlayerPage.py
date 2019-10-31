
from test.pages.ActivityPage import ActivityPage
from selenium.webdriver.common.by import By
from test.common.Common import *
import time
import win32api
import win32con
import pyperclip

class PlayerPage(ActivityPage):
    #运动员添加按钮
    def add_button(self):
       return self.find_element(By.XPATH,'//*[@id="form"]/div[2]/a')
    #运动员添加表单
    def player_name_element(self):
       return  self.find_element(By.ID,'name')
    def play_credentials_element(self):
       return self.find_element(By.ID,'credentials')
    def play_number_book_element(self):
       return self.find_element(By.ID,'number_book')
    def play_group_element(self):
       return self.find_element(By.ID, 'group')
    def unit_element(self):
        return self.find_element(By.ID, 'unit')
    def initials_element(self):
        return self.find_element(By.ID, 'initials')
    def si_card_id_element(self):
        return self.find_element(By.ID, 'si_card_id')
    def  country_element(self):
        return self.find_element(By.ID, 'country')
    def  phone_element(self):
        return self.find_element(By.ID, 'phone')
    def  team_element(self):
        return self.find_element(By.ID, 'team')
    def play_beginDate_element(self):
        return self.find_element(By.ID, 'beginDate')
    def begin_date_hh_element(self):
        return self.find_element(By.NAME, 'begin_date_hh')
    def begin_date_mm_element(self):
        return self.find_element(By.NAME, 'begin_date_mm')
    def begin_date_ss_element(self):
        return self.find_element(By.NAME, 'begin_date_ss')
    def play_endDate_element(self):
        return self.find_element(By.ID, 'endDate')
    def end_date_hh_element(self):
        return self.find_element(By.NAME, 'end_date_hh')
    def end_date_mm_element(self):
        return self.find_element(By.NAME, 'end_date_mm')
    def end_date_ss_element(self):
        return self.find_element(By.NAME, 'end_date_ss')



    def btnSave_button(self):
        return self.find_element(By.ID, 'btnSave')

    def player_device_id_element(self):
        return self.find_element(By.ID, 'device_id')
    def btnSearch_button(self):
        return self.find_element(By.ID, 'btnSearch')

#点击运动员添加按钮
    def add(self):
       return self.add_button().click()

    # 运动员添加
    def player_add(self,play_name=None,play_credentials=None,play_number_book=None,play_group=None,unit=None,initials=None,si_card_id=None,country=None,phone=None,team=None):

        self.player_name_element().send_keys(play_name)
        self.play_credentials_element().send_keys(play_credentials)
        self.play_number_book_element().send_keys(play_number_book)
        self.play_group_element().send_keys(play_group)
        self.unit_element().send_keys(unit)
        self.initials_element().send_keys(initials)
        self.si_card_id_element().send_keys(si_card_id)
        self.country_element().send_keys(country)
        self.phone_element().send_keys(phone)
        self.team_element().send_keys(team)
    #运动员添加列表-日期选择器
    def datetimepicker(self):
        self.play_beginDate_element().click()
        self.find_element(By.XPATH, '/ html / body / div[2] / div[3] / table / tfoot / tr / th').click()
        self.play_endDate_element().click()
        self.find_element(By.XPATH, '/html/body/div[3]/div[3]/table/tfoot/tr/th').click()

#运动员按case添加
    def player_add01(self, username, credentials, number_book, group,unit,initials,si_card_id,country,phone,team,beginDate,begin_date_hh,begin_date_mm,begin_date_ss,play_endDate,end_date_hh,end_date_mm,end_date_ss):
       if username != None:
           self.player_name_element().send_keys(username)
       if credentials != None:
           self.play_credentials_element().send_keys(credentials)
       if number_book != None:
           self.play_number_book_element().send_keys(number_book)
       if group != None:
           self.play_group_element().send_keys(group)
       if unit != None:
           self.unit_element().send_keys(unit)
       if initials != None:
           self.initials_element().send_keys(initials)
       if si_card_id != None:
           self.si_card_id_element().send_keys(si_card_id)
       if country != None:
           self.country_element().send_keys(country)
       if phone != None:
           self.phone_element().send_keys(phone)
       if team != None:
           self.team_element().send_keys(team)
       if beginDate != None:
           self.play_beginDate_element().send_keys(beginDate)
           self.play_beginDate_element().click()
       if begin_date_hh != None:
           self.begin_date_hh_element().send_keys(begin_date_hh)
       if begin_date_mm != None:
           self.begin_date_mm_element().send_keys(begin_date_mm)
       if begin_date_ss != None:
           self.begin_date_ss_element().send_keys(begin_date_ss)
       if play_endDate != None:
           self.play_endDate_element().send_keys(beginDate)
           self.play_endDate_element().click()
       if end_date_hh != None:
           self.end_date_hh_element().send_keys(end_date_hh)
       if end_date_mm != None:
           self.end_date_mm_element().send_keys(end_date_mm)
       if end_date_ss != None:
           self.end_date_ss_element().send_keys(end_date_ss)
       #
       # try:
       #  self.find_element(By.XPATH,'/html/body/div[2]/div[3]/table/tfoot/tr/th').click()
       #  print('必填项为空/号码簿错误')
       # except:
       #  print('添加成功')
       self.find_element(By.ID,'btnSave').click()
       try:
        self.parentframe()
        self.find_element(By.XPATH,'/ html / body / div[5] / div[3] / a').click()
        print('必填项为空/号码簿重复')
       except:
           print('添加成功')

#


    # 运动员按case查询
    def player_search(self, username, number_book,device_id):
       if username != None:
           player_name_element = self.find_element(By.ID, 'name')
           player_name_element.send_keys(username)
       if number_book != None:
           play_number_book_element = self.find_element(By.ID, 'number_book')
           play_number_book_element.send_keys(number_book)
       if device_id != None:
           play_device_id_element = self.find_element(By.ID, 'device_id')
           play_device_id_element.send_keys(device_id)


    #批量发放按钮
    def player_device_provide_button(self):
        return  self.find_element(By.XPATH,'//*[@id="form"]/div[4]/div/div[2]/a')
    def player_device_provide(self):
        return  self.player_device_provide_button().click()

    #运动员查询清理
    def search_clear(self):
        self.player_name_element().clear()
        self.play_number_book_element().clear()
        self.player_device_id_element().clear()

    def save(self):
        return self.btnSave_button().click()
    #运动员下拉菜单组别查询
    def group_menu(self):
        i = 1
        while i > 0:
            i =i + 1
            menu=self.find_element(By.XPATH, '// *[ @ id = "form"] / div[1] / div[4] / div[1] / div')
            menu.click()
            try:
                group_text = self.find_element(By.XPATH,
                                               "// *[ @ id = 'form']/div[1]/div[4]/div[1]/div/div/ul/li[" + str(
                                                   i) + "]/a/span[1]").text
                group_seleck=self.find_element(By.XPATH,
                               "// *[ @ id = 'form'] / div[1] / div[4] / div[1] / div / div / ul / li["+str(i)+"] / a / span[1]")
                group_seleck.click()
            except:
                break
            print(i)
            print(group_text)
            self.search()
 # 运动员下拉菜单单位查询
    def unit_menu(self):
        i = 1
        while i > 0:
            i =i + 1
            menu=self.find_element(By.XPATH, '// *[ @ id = "form"] / div[1] / div[4] / div[2] / div')
            menu.click()
            try:
                unit_text = self.find_element(By.XPATH,
                                               "// *[ @ id = 'form']/div[1]/div[4]/div[2]/div/div/ul/li[" + str(
                                                   i) + "]/a/span[1]").text
                unit_seleck=self.find_element(By.XPATH,
                               "// *[ @ id = 'form'] / div[1] / div[4] / div[2] / div / div / ul / li["+str(i)+"] / a / span[1]")
                unit_seleck.click()
            except:
                break
            print(i)
            print(unit_text)
            self.search()
   # 运动员下拉菜单国家/地区查询
    def country_menu(self):
        i = 1
        while i > 0:
            i =i + 1
            menu=self.find_element(By.XPATH, '// *[ @ id = "form"] / div[1] / div[4] / div[3] / div')
            menu.click()
            try:
                country_text = self.find_element(By.XPATH,
                                               "// *[ @ id = 'form']/div[1]/div[4]/div[3]/div/div/ul/li[" + str(
                                                   i) + "]/a/span[1]").text
                country_seleck=self.find_element(By.XPATH,
                               "// *[ @ id = 'form'] / div[1] / div[4] / div[3] / div / div / ul / li["+str(i)+"] / a / span[1]")
                country_seleck.click()
            except:
                break
            print(i)
            print(country_text)
            self.search()

#运动员查询按钮点击
    def search(self):
        self.btnSearch_button().click()
        try:
            a = self.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div/div[1]/div[2]/div').text
            print(a)
            if a=="无数据":
                print("查询失败")
        except:
            print("查询成功")
#运动员导入错误提示
    def error_message_import(self):
        # self.find_element(By.CLASS_NAME,'layui-layer-content').text
        self.find_element(By.CLASS_NAME,'layui-layer-btn0').click()
        print('文件中、或文件与已有运动员的号码簿重复，未能导入成功。')
     #运动员批量发放错误提示
    def error_message_device(self):
        # self.find_element(By.CLASS_NAME,'layui-layer-content').text
        self.find_element(By.CLASS_NAME,'layui-layer-btn0').click()
        print('该设备没有回收或导入信息中存在相同的设备')


 #运动员导入按钮
    def import_player_button(self):
        return self.find_element(By.XPATH, '// *[ @ id = "form"] / div[3] / a[1]')
    def import_player(self):
        self.import_player_button().click()

    # 运动员导出按钮
    def export_player_button(self):
        return self.find_element(By.ID, 'out')
    def export_player(self):
        self.export_player_button().click()

#批量发放按钮
    def provide_device_button(self):
        return self.find_element(By.XPATH, '//*[@id="form"]/div[4]/div/div[2]/a')
    def provide_device(self):
        self. provide_device_button().click()
    #导入按钮
    def import_device_button(self):
        return self.find_element(By.XPATH, '// *[ @ id = "form"] / div[2] / a')
    def import_device(self):
        self.import_device_button().click()

    #运动员编辑按钮
    def edit_button(self):
        return self.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[19]/div/a[1]')
    def edit(self):
        return self.edit_button().click()
    def player_edit(self, play_name=None, play_credentials=None, play_number_book=None, play_group=None):
        self.player_name_element().send_keys(play_name)
        self.play_credentials_element().send_keys(play_credentials)
        self.play_number_book_element().send_keys(play_number_book)
        self.play_group_element().send_keys(play_group)
        self.find_element(By.ID, 'btnSave').click()

    #运动员图片设置
    def img_button(self):
        return self.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[19]/div/a[2]')
    def img(self):
        return self.img_button().click()

    #运动员图片删除


    #列表多选框
    def player_select(self):
        return self.find_element(By.CSS_SELECTOR,"th.layui-table-col-special > div > div > i").click()

    #批量修改图片
    def add_img(self):
        self.find_element(By.XPATH,'//*[@id="form"]/div[4]/div/div[3]/a').click()
    def add_imgs(self):
        self.find_element(By.ID, "upload_img").send_keys('F:\location\产品测试\自动化测试\\autoTest\img\\64x64test.png')
        time.sleep(3)
        self.find_element(By.ID, 'btnSave').click()

    #批量删除
    def player_delete_button(self):
        return self.find_element(By.XPATH,'//*[@id="form"]/div[4]/div/div[1]/a')
    def player_delete(self):
        return self.player_delete_button().click()

    #批量删除图片
    def delete_img_button(self):
        return self.find_element(By.CSS_SELECTOR,'div.pull-right:nth-child(4) > a:nth-child(1)')
    def delete_img(self):
        return self.delete_img_button().click()

    # 确定删除按钮
    def delete_confirm_button(self):
        return self.find_element(By.CSS_SELECTOR, '.layui-layer-btn0')
    def delete_confirm(self):
        return self.delete_confirm_button().click()




if __name__ == '__main__':
    a =PlayerPage()
    a.login()
    a.iframe1()
    a.base_setting()
    a.iframe0()
    # a.player_edit()
    # a.player_select()
    # a.add_img()
    # a.iframe2()
    # a.add_imgs()
    # a.dropdown_menu_open()
    a.dropdown_menu()

    # a.player_delete()
    # a.delete_confirm()
    # a.player_select()
    # a.delete_img()
    # a.parentframe()
    # a.delete_confirm()

        # a.add()
        # a.iframeauto()
        # a.player_add('111','1111','11111','111111','2019-09-20')
    # a.player_name_serach('1')
    # a.serach()
    # a.serach_clear()
    # # a.player_number_book_serach('683')
    # # a.serach()
    # a.import_player()
    # a.UpLoad_File('F:\location\产品测试\自动化测试\\autoTest\data\副本1.12duoren2019-09-26.xlsx' )
    # a.provide_device()
    # a.parentframe()
    # a.iframeauto01()
    # a.import_device()
    # a.UpLoad_File('F:\location\产品测试\自动化测试\\autoTest\data\副本批量发放模板2019-09-26.xlsx')












