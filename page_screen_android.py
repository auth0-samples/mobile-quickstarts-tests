import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *


class PageScreen:

    def __init__(self, driver):
        self.driver = driver

    def log_user(self):

        login_button = WebDriverWait(self.driver.instance, 15).until(
            EC.visibility_of_element_located((
                MobileBy.XPATH, "//android.widget.Button"
            ))
        )
        login_button.click()

        self.switch_context("WEBVIEW_chrome")
        self.fill_user_data()

        assert 'Logged' in self.verify_user_login()

    def switch_context(self, new_context):

#TODO: Search dynamic wait for the context switch
        time.sleep(10)

        c_context = self.driver.instance.mobile.contexts
        # print(c_context)
        self.driver.instance.switch_to.context(new_context)

    def fill_user_data(self):
        username = WebDriverWait(self.driver.instance, 7000).until(
            EC.visibility_of_element_located((
                MobileBy.XPATH, "//input[@name='username']"
            ))
        )
        password = WebDriverWait(self.driver.instance, 2).until(
            EC.visibility_of_element_located((
                MobileBy.XPATH, "//input[@name='password']"
            ))
        )
        username.send_keys(login_user)
        password.send_keys(login_password)
        button_login = WebDriverWait(self.driver.instance, 2).until(
            EC.visibility_of_element_located((
                MobileBy.XPATH, "//button[@name='submit']"
            ))
        )
        button_login.click()

    def verify_user_login(self):
        self.switch_context("NATIVE_APP")

        logged_text = WebDriverWait(self.driver.instance, 15).until(
            EC.visibility_of_element_located((
                MobileBy.XPATH, "//android.widget.TextView"
            ))
        )

        return logged_text.text
