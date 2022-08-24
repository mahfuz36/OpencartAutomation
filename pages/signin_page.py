import time

from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SignIn:

    def __init__(self, driver):
        self.driver = driver

    def signin_auto_practice(self):
        # sn_btn = self.driver.find_element(By.XPATH, "//*[@id='header']/div[2]/div/div/nav/div[1]")
        sn_btn = self.driver.find_element(By.LINK_TEXT, "Sign in").click()
        time.sleep(2)

        # my_leave = driver.find_element(By.LINK_TEXT, 'My Leave')
        # my_leave.click()
        # time.sleep(3)
