from driver import browser

import time
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()
