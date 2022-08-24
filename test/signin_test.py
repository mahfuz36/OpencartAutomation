from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
from pages.signin_page import SignIn
from pages.sign_up_page import SignInAndCreate
from Utils.param import Configuration


class SignInTest(unittest.TestCase):
    def test_signin(self):
        global driver
        baseUrl = "http://automationpractice.com/index.php"
        driver = Configuration.BROWSER
        # driver.implicitly_wait(5)
        driver.get(baseUrl)
        time.sleep(2)

        # signin = SignIn(driver)
        # signin.signin_auto_practice()

        signup = SignInAndCreate(driver,)
        # signup.sign_up()

        # signup = SignInAndCreate(driver)
        signup.enterEmail("abcd1@gmail.com")
