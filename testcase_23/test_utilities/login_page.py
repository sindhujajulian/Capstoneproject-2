from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from test_data import credentials
from test_locators.all_locators import LoginPageLocators


class Orangehrm:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.my_wait = WebDriverWait(self.driver, 10)
        self.locators = LoginPageLocators
        self.url = credentials.url
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(5)

    def login_to_orangehrm(self):
        """
        Log into OrangeHRM
        :return:
        """
        username_webelement = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.username_xpath)))
        username_webelement.send_keys(credentials.username)

        password_webelement = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.password_xpath)))
        password_webelement.send_keys(credentials.password)

        login_button_element = self.my_wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.login_button_xpath)))
        login_button_element.click()
        sleep(5)

    def admin_page_menu(self):
        self.login_to_orangehrm()

        list = credentials.list_1
        length = len(list)
        list2 = []

        for i in range(1, length + 1):
            webelements_admin_menu = self.my_wait.until(EC.visibility_of_element_located(
                (By.XPATH, self.locators.admin_menu_xpath + "[" + str(i) + "]")))
            expected = list[(i - 1)]
            if webelements_admin_menu == expected:
                list2.append("True")
        else:
            list2.append("False")

        set1 = set(list2)
        if len(set1) == 1:
            return "Successful"