from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from login_page import LoginPage
import time

class Clue(LoginPage):

    #进入搜索引擎url
    clue_url = '/clue/index'
    #公司名称id
    corporate_name_id = ('company_tag')
    #提交
    sub_xpath = ('/html/body/div[11]/div[2]/div/div[2]/input')
    #线索下载
    download_id = ('downBtn')
    #分组名称
    group_name_id = ('inputGroupName')
    #提交下载
    sub_download_xpath = ('/html/body/div[12]/input')

    #检查点
    number_class = ('number')




    def clue_url_get(self):
        return self.driver.get(self.type_url + self.clue_url)

    def corporate_name(self):
        return self.by_id(self.corporate_name_id).send_keys('科技')

    def enter_kesy(self):
        return self.by_id(self.corporate_name_id).send_keys(Keys.ENTER)

    def js_page(self):
        target = self.by_id("downBtn")
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def sub(self):
        return self.by_xpath(self.sub_xpath).click()



    #下载

    def clue_download(self):
        return self.by_id(self.download_id).click()

    def group_name(self):
        return self.by_id(self.group_name_id).send_keys('线索下载')

    def sub_download(self):
        return self.by_xpath(self.sub_download_xpath).click()

    #检查点
    def assert_number(self):
        return self.by_class_name(self.number_class).text

    #线索搜索
    def clue_actiom(self):
        self.open()
        self.login_actiom(self.user, self.pwd)
        time.sleep(2)
        self.clue_url_get()
        self.corporate_name()
        self.enter_kesy()
        self.js_page()
        self.sub()
        time.sleep(2)


    #线索下载
    def clue_download_actiom(self):
        self.open()
        self.login_actiom(self.user, self.pwd)
        time.sleep(2)
        self.clue_url_get()
        self.corporate_name()
        self.enter_kesy()
        self.js_page()
        self.sub()
        time.sleep(2)
        self.js_page()
        self.clue_download()
        self.group_name()
        time.sleep(2)
        self.sub_download()
        time.sleep(60)
        




