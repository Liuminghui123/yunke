from base import Base
import time

class AssertPage(Base):


    def login_success_user(self):
        return self.driver.title


    def text_alert(self):
        return self.a_alert().text


