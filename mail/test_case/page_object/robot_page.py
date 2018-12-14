from login_page import LoginPage
import time


class Robot(LoginPage):
    '''机器人'''
    robot_url = '/robotPlan/robotTask'

    new_task_xpath = '//*[@id="main"]/div[1]/div/a'

    task_name_xpath = '//*[@id="main"]/div[2]/div[1]/div[2]/input'

    robot_bumber_xpath = '//*[@id="main"]/div[2]/div[2]/div[2]/input'

    start_time_id = 'timetext'
    end_time_id = 'timetext1'

    task_file_xpath = '//*[@id="main"]/div[2]/div[5]/div[2]/div'
    task_file_xpath_1 = '//*[@id="taskSouces"]/div[2]/div/label[1]'
    task_file_btn_xpath = '//*[@id="taskSouces"]/div[3]/div/input[1]'

    template_xpath = '//*[@id="main"]/div[2]/div[6]/div[2]/select'
    template_xpath_1 = '//*[@id="main"]/div[2]/div[6]/div[2]/select/option[2]'

    btn_xpath = '//*[@id="main"]/div[2]/div[8]/div/input[1]'

    def new_task(self):
        return self.by_xpath(self.new_task_xpath).click()

    def task_name(self, text):
        return self.by_xpath(self.task_name_xpath).send_keys(text)

    def robot_bumber(self, text):
        return self.by_xpath(self.robot_bumber_xpath).send_keys(text)

    def task_file(self):
        return self.by_xpath(self.task_file_xpath).click()

    def task_file_1(self):
        return self.by_xpath(self.task_file_xpath_1).click()

    def task_file_btn(self):
        return self.by_xpath(self.task_file_btn_xpath).click()

    def template(self):
        return self.by_xpath(self.template_xpath).click()

    def template_1(self):
        return self.by_xpath(self.template_xpath_1).click()

    def btn(self):
        return self.by_xpath(self.btn_xpath).click()

    def robot_new_task_actiom(self, name, bumder):
        self.open()
        self.login_actiom(self.user, self.pwd)
        time.sleep(2)
        self.driver.get(self.type_url + self.robot_url)
        self.new_task()
        self.task_name(name)
        self.robot_bumber(bumder)
        self.task_file()
        self.task_file_1()
        self.task_file_btn()
        time.sleep(2)
        self.template()
        self.template_1()

        self.btn()
