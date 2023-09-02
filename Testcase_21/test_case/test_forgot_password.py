from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from test_data import credentials
from test_locators.all_locators import Loginlocators

class OrangeHrm:

    def __init__(self):
       self.all_locators = Loginlocators()
       self.driver = webdriver.Chrome()
       self.driver.get(credentials.url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(10)


    def Forgot_password(self):
       """
      find the webelement for forgot password,and click it
       :return:

       """

       forgotpassword_webelement = self.driver.find_element(By.XPATH,self.all_locators.forgot_password_locator)
       forgotpassword_webelement.click()
       sleep(3)

       wait = WebDriverWait(self.driver,20)
       username_webelement = wait.until(EC.element_to_be_clickable((By.XPATH, self.all_locators.username_locator)))


       #username_webelement = self.driver.find_element(By.XPATH,self.all_locators.username_locator)
       username_webelement.click()
       username_webelement.send_keys(credentials.username)
       sleep(3)

       reset_password_webelement = self.driver.find_element(By.XPATH,self.all_locators.reset_password_locator)
       reset_password_webelement.click()
       sleep(3)


def test_forgot_password():
   orange_hrm = OrangeHrm()
   orange_hrm.Forgot_password()


if __name__ == '__main__':
    obj = OrangeHrm()
    obj.Forgot_password()
