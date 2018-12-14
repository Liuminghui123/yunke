from login_page import LoginPage
import time
import os

class CustomerTaskPage(LoginPage):
    # 客户列表----创建任务
    customer_url = '/customer/index'
    # 选择本页
    choice_xpath = ('//*[@id="table-list"]/thead/tr/th[1]/i')
    # 添加任务
    add_task_xpath = ('/html/body/div[17]/div[1]/a')
    # 新建任务
    new_task_xpath = ('/html/body/div[17]/div[1]/div[1]/div[1]/span')
    # 任务名称
    task_name_id = ('newplanname')
    task_name = ('客户新建任务')
    # 开始时间
    choice_time_id = ('timetext4')
    # 执行销售
    choice_sale_xpath = ('//*[@id="applyBox-1"]/div[2]/div/div[2]/div[1]')
    sale_xpath = ('//*[@id="addTask-staffZtree_1_a"]')
    dete_xpaht = ('//*[@id="applyBox-1"]/div[2]/div/div[2]/div[2]/div/input')
    # 提交
    customer_sub_xpath = ('//*[@id="applyBox-1"]/input[2]')


    # 导入客户

    import_text_id = 'exporter'
    import_browse_id = 'cusfile'
    #获取当前路径
    import_text_path = os.path.dirname(os.path.realpath(__file__))
    import_text_url = os.path.join(import_text_path, "data" , "import_test.xls")

    import_but_id = 'changerBtn-2'

    #获取导入成功信息
    import_yes_id ='sysResult'

    #获取失败信息
    assertt_yes_id = 'sysResult'
    assert_no_xpath = '//*[@id="errorUpload"]/div[2]/div[1]'
    assert_no_xpath1 = '//*[@id="errorUpload"]/div[2]/div[3]/div[1]'
    assert_no_xpath2 = '//*[@id="errorUpload"]/div[2]/div[3]/div[2]'

    #失败验证
    list1 = ['','','']
    list2 = ['成功：0 条 ，失败：1 条',
             '表中客户手机号码与系统录入客户手机号码重复',
             '手机（必填）:手机号：[13513351889]重复']
    close_tips_xpath = '//*[@id="errorUpload"]/div[1]/a'


    # 任务页面
    task_url = '/plan/index'
    # 进行中任务
    conduct_task_xpath = ('/html/body/div[10]/div[1]/div[2]/em')
    # 终止任务
    stop_task_id = ('overmission')


    # 获取本地时间
    def choice_time(self):
        return time.strftime("%Y-%m-%d", time.localtime())

    #导入成功验证
    def assert_yse(self):
        return self.by_id(self.import_yes_id).text

    #关闭失败原因
    def close_tips(self):
        return self.by_xpath(self.close_tips_xpath).click()

    def assert_no(self):
        self.list1[0] = self.by_xpath(self.assert_no_xpath).text
        self.list1[1] = self.by_xpath(self.assert_no_xpath1).text
        self.list1[2] = self.by_xpath(self.assert_no_xpath2).text
        return self.list1



    def customer_task_actiom(self):
        self.open()
        self.login_actiom(self.user, self.pwd)
        time.sleep(2)
        self.driver.get(self.type_url + self.customer_url)
        self.by_xpath(self.choice_xpath).click()
        self.by_xpath(self.add_task_xpath).click()
        time.sleep(2)
        self.by_xpath(self.new_task_xpath).click()
        self.by_id(self.task_name_id).send_keys(self.task_name)
        self.by_id(self.choice_time_id).send_keys(self.choice_time())
        self.by_xpath(self.choice_sale_xpath).click()
        self.by_xpath(self.sale_xpath).click()
        self.by_xpath(self.dete_xpaht).click()
        self.by_xpath(self.customer_sub_xpath).click()

    def stop_task_actiom1(self):
        self.open()
        self.login_actiom(self.user, self.pwd)
        time.sleep(2)
        self.driver.get(self.type_url + self.task_url)
        self.by_xpath(self.conduct_task_xpath).click()
        self.by_id(self.stop_task_id).click()

    #客户列表导入文件
    def import_text_actiom(self):
        self.open()
        self.login_actiom(self.user,self.pwd)
        time.sleep(2)
        self.driver.get(self.type_url + self.customer_url)
        self.by_id(self.import_text_id).click()
        self.by_id(self.import_browse_id).send_keys(self.import_text_url)
        self.by_id(self.import_but_id).click()





