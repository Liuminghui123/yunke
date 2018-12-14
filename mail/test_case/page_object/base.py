from selenium import webdriver
import time
import unittest

class Base(object):
    type_url = 'http://123.57.222.150:8083/testShowField/'

    def __init__(self, driver, url='/home/login'):
        self.driver = driver
        self.base_url = url

    def _opne(self):
        url_ = self.type_url + self.base_url
        self.driver.get(url_)
        time.sleep(2)
        assert self.driver.current_url == url_

    def open(self):
        self._opne()

    def by_id(self, _id):
        return self.driver.find_element_by_id(_id)

    def by_class_name(self, _class_name):
        return self.driver.find_element_by_class_name(_class_name)

    def by_xpath(self, _xpath):
        return self.driver.find_element_by_xpath(_xpath)

    def by_link_text(self,_text):
        return self.driver.find_element_by_link_text(_text)

    def iframe(self, _iframe):
        return self.driver.switch_to.frame(_iframe)

    def iframe_out(self):
        return self.driver.switch_to.defauit_content()

    def a_alert(self):
        return self.driver.switch_to.alert







