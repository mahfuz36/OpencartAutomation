import unittest
import time
from pages.sign_up_page import SignInAndCreate
from Utils.param import Configuration


class SignInTest(unittest.TestCase):
    def test_signin(self):
        baseUrl = "http://automationpractice.com/index.php"
        driver = Configuration.BROWSER
        # driver.implicitly_wait(5)
        driver.get(baseUrl)
        time.sleep(2)


        signup = SignInAndCreate(driver)
        signup.sign_up()
        time.sleep(2)
        signup.enterEmail("maf12344@gmail.com")
