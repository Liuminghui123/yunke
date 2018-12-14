from login_page import LoginPage
from myunit import MyTest
from assert_page import AssertPage
import time
import unittest
class LoginTest(MyTest):
    '''登录测试'''
    def test_login_user_pwd_null(self):
        '''账号，密码空'''
        po = LoginPage(self.driver)
        po.open()
        po.login_actiom('', '')
        time.sleep(2)
        po2 = AssertPage(self.driver)
        self.assertEqual(po2.text_alert(), '请输入手机号')

    def test_login_user_null(self):
        '''账号空'''
        po = LoginPage(self.driver)
        po.open()
        po.login_actiom('', '111111')
        time.sleep(2)
        po2 = AssertPage(self.driver)
        self.assertEqual(po2.text_alert(), '请输入手机号')

    def test_login_pwd_null(self):
        '''密码空'''
        po = LoginPage(self.driver)
        po.open()
        po.login_actiom('13439281553', '')
        time.sleep(2)
        po2 = AssertPage(self.driver)
        self.assertEqual(po2.text_alert(), '请输入密码')

    def test_login_user_pwd_error(self):
        '''账号，密码错误'''
        po = LoginPage(self.driver)
        po.open()
        po.login_actiom('111111', '123456')
        time.sleep(2)
        po2 = AssertPage(self.driver)
        self.assertEqual(po2.text_alert(), '账号或密码错误')

    def test_login_user_error(self):
        '''账号错误'''
        po = LoginPage(self.driver)
        po.open()
        po.login_actiom('111111', '111111')
        time.sleep(2)
        po2 = AssertPage(self.driver)
        self.assertEqual(po2.text_alert(), '账号或密码错误')

    def test_login_pwd_error(self):
        '''密码错误'''
        po = LoginPage(self.driver)
        po.open()
        po.login_actiom('13439281553', '123456')
        time.sleep(2)
        po2 = AssertPage(self.driver)
        self.assertEqual(po2.text_alert(), '账号或密码错误')

    def test_login_pwd_error(self):
        '''正常登录'''
        po = LoginPage(self.driver)
        po.open()
        po.login_actiom('13439281553', '1111111')
        time.sleep(2)
        po2 = AssertPage(self.driver)
        self.assertEqual(po2.login_success_user(), '个人客户')

