from myunit import MyTest
from customers_page import CustomersPage
from assert_page import AssertPage
from customer_task_page import CustomerTaskPage
import time


class CustomersTest(MyTest):
    '''客户列表'''

    # def test_001_new_customer(self):
    #     '''新建客户测试'''
    #     po = CustomersPage(self.driver)
    #     po.new_customer_actiom('12345678936', '12345678936')
    #     self.assertEqual(po.assert_number(), '12345678936   ')
    #
    # def test_002_repeat_new_customer(self):
    #     '''重复新建客户测试'''
    #     po = CustomersPage(self.driver)
    #     po.repeat_new_customer_actiom('12345678936', '12345678936')
    #     po2 = AssertPage(self.driver)
    #     time.sleep(2)
    #     self.assertEqual(po2.text_alert(), '手机号已存在')

    def test_003_delete(self):
        '''删除客户测试'''
        po = CustomersPage(self.driver)
        po.delete_actiom('12345678936')
        po2 = AssertPage(self.driver)
        time.sleep(2)
        self.assertEqual(po2.text_alert(), '删除成功')

    def test_004_new_task(self):
        '''客户列表添加任务'''
        po = CustomerTaskPage(self.driver)
        po.customer_task_actiom()
        time.sleep(2)
        po2 = AssertPage(self.driver)
        self.assertEqual(po2.text_alert(), '添加成功')



    def test_006_stop_task(self):
        '''终止任务'''
        po = CustomerTaskPage(self.driver)
        po.stop_task_actiom1()
        time.sleep(2)
        po.a_alert().accept()
        time.sleep(2)
        po2 = AssertPage(self.driver)
        self.assertEqual(po2.text_alert(), '成功终止任务')

    def test_007_import_text(self):
        '''客户列表导入数据'''
        po = CustomerTaskPage(self.driver)
        po.import_text_actiom()
        time.sleep(2)
        self.assertEqual(po.assert_yse(), '导入成功：共导入1条数据')
        po2 = CustomersPage(self.driver)
        po2.delete_actiom(13513351889)

    # def test_008_import_text(self):
    #     '''客户列表重复导入数据'''
    #     po = CustomerTaskPage(self.driver)
    #     po.import_text_actiom()
    #     time.sleep(2)
    #     self.assertEqual(po.assert_no(), po.list2)
    #     po.close_tips()
    #     po2 = CustomersPage(self.driver)
    #     po2.delete_actiom(13513351889)































