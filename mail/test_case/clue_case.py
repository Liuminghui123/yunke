from clue_page import Clue
from myunit import MyTest
from assert_page import AssertPage
from customer_task_page import CustomerTaskPage
import time
import unittest

class ClueTest(MyTest):
    '''线索测试'''
    def test_clue(self):
        '''搜索数据正常显示'''
        po = Clue(self.driver)
        po.clue_actiom()
        self.assertNotEqual(po.assert_number(), '')

    def test_clue_download(self):
        '''线索下载测试'''
        po = Clue(self.driver)
        self.actiom = po.clue_download_actiom()
        po2 = AssertPage(self.driver)
        self.assertEqual(po2.text_alert(), '成功下载:2000条')

