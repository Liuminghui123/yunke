from login_page import LoginPage
import time


class CustomersPage(LoginPage):
    '''客户列表新建客户'''
    # 管理帐号

    # 进入客户列表
    CustomerList_url = '/customer/index'
    add_customer_id = ('add_customer')
    user_name_id = ('addcustomerName')
    user_number_id = ('addcellPhone')
    # 提交
    btn_xpath = '//*[@id="applyBox-2"]/input'

    # 搜索
    concontent_id = ('concontent')

    # 提交搜索
    search_icon_class = ('search-icon')

    # 检查手机号
    number_xpath = ('//*[@id="table-list"]/tbody/tr[1]/td[3]')

    # 选择
    choice_xpath = ('//*[@id="table-list"]/tbody/tr[1]/td[1]/i')

    # 删除
    dele_class = ('b2')

    # 确定
    yes_xpath = ('//*[@id="changer-box-1"]/input[1]')

    # 进入搜索引擎url
    def customer_url_get(self):
        return self.driver.get(self.type_url + self.CustomerList_url)

    def add_customer(self):
        return self.by_id(self.add_customer_id).click()

    def user_name(self, text):
        return self.by_id(self.user_name_id).send_keys(text)

    def user_number(self, number_text):
        return self.by_id(self.user_number_id).send_keys(number_text)

    def btu(self):
        return self.by_xpath(self.btn_xpath).click()

    def concontent(self, text):
        return self.by_id(self.concontent_id).send_keys(text)

    def search_icon(self):
        return self.by_class_name(self.search_icon_class).click()

    # 检查点
    def assert_number(self):
        return self.by_xpath(self.number_xpath).text

    def for_Location(self):
        for i in range(5):
            try:
                self.by_xpath(self.number_xpath)
                break
            except:
                time.sleep(5)
                self.driver.refresh()

    def choice(self):
        return self.by_xpath(self.choice_xpath).click()

    def dele(self):
        return self.by_class_name(self.dele_class).click()

    def yes(self):
        return self.by_xpath(self.yes_xpath).click()

    def new_customer_actiom(self,username,number):
        '''新建客户'''
        self.open()
        self.login_actiom(self.user, self.pwd)
        time.sleep(2)
        self.customer_url_get()
        self.add_customer()
        self.user_name(username)
        self.user_number(number)
        self.btu()
        self.concontent(number)
        self.search_icon()
        self.for_Location()

    def delete_actiom(self, number):
        '''删除客户'''
        self.open()
        self.login_actiom(self.user, self.pwd)
        time.sleep(5)
        self.customer_url_get()
        self.concontent(number)
        self.search_icon()
        self.for_Location()
        self.choice()
        self.dele()
        self.yes()

    def repeat_new_customer_actiom(self, username, number):
        '''重复新建客户测试'''
        self.open()
        self.login_actiom(self.user, self.pwd)
        time.sleep(5)
        self.customer_url_get()
        self.add_customer()
        self.user_name(username)
        self.user_number(number)
        self.btu()
