from myunit import MyTest
from assert_page import AssertPage
from robot_page import Robot

class RobotTest(MyTest):
    '''机器人'''
    def test_name_null(self):
        po = Robot(self.driver)
        po.robot_new_task_actiom('','')
        po2 = AssertPage(self.driver)
        self.assertEqual(po2.text_alert(), '任务名称不能为空')