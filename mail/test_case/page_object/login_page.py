from base import Base
import time

class LoginPage(Base):
    user = '13146866232'
    pwd = '111111'

    user_sale = '13439281553'
    pwd_sale = '111111'


    user_id = ('uid')
    pwd_id = ('pwd')
    button_id = ('login_button')

    def login_user(self, text):
        self.by_id(self.user_id).send_keys(text)

    def login_pwd(self, text):
        self.by_id(self.pwd_id).send_keys(text)

    def login_button(self):
        self.by_id(self.button_id).click()


    def login_actiom(self, username, password):
        self.login_user(username)
        self.login_pwd(password)
        self.login_button()

    def logi_sale_actiom(self,username, password):
        self.login_user(username)
        self.login_pwd(password)
        self.login_button()