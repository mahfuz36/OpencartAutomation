from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
from pages.login1_page import LoginPage
from pages.payment_page import PaymentShoping
from pages.tshirt_page import TshirtShoping
from pages.signin_page import SignIn
from Utils import excel_utils
from Utils.param import Configuration

class TshirtTest(unittest.TestCase):
    global driver
    def test_tshirt_shopping(self):
        baseUrl = Configuration.BASE_URL
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.implicitly_wait(5)
        driver.get(baseUrl)
        time.sleep(3)

        signin = SignIn(driver)
        signin.signin_auto_practice()
        # """"
        # file = 'F:\PeoplenTech QAT Course\Automationpractice\dataDataFile.xlsx'
        # sheet = 'login'
        #
        # number_of_rows = excel_utils.get_row_count(file, sheet)
        #
        # for r in range(2, number_of_rows + 1):
        #     email = excel_utils.read_data(file, sheet, r, 1)
        #     password = excel_utils.read_data(file, sheet, r, 2)
        # """

        lp = LoginPage(driver)
        lp.login_auto_practice("mahfuzf@gmail.com", "mahfuz")
        print("Login Successful")
        time.sleep(3)

        ts = TshirtShoping(driver)
        ts.tshirt_page()
        time.sleep(3)

        po = PaymentShoping(driver)
        po.payment_page()

        driver.close()
        driver.quit()

# if __name__ == '__main__':
#     unittest.main()
