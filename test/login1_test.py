from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
from Utils.param import Configuration
from pages.login1_page import LoginPage
from Utils import excel_utils
from pages.signin_page import SignIn


class LoginTest(unittest.TestCase):

    def test_login(self):
        baseUrl = Configuration.BASE_URL
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.implicitly_wait(2)
        driver.get(baseUrl)
        time.sleep(3)

        signin = SignIn(driver)
        signin.signin_auto_practice()

        file = 'F:\PeoplenTech QAT Course\Automationpractice\data\DataFile.xlsx'
        sheet = 'login'

        number_of_rows = excel_utils.get_row_count(file, sheet)

        for r in range(2, number_of_rows + 1):
            email = excel_utils.read_data(file, sheet, r, 1)
            password = excel_utils.read_data(file, sheet, r, 2)

            lp = LoginPage(driver)
            lp.login_auto_practice(email, password)
            print("Login Successful")
        time.sleep(3)
        driver.close()
        driver.quit()


#     @classmethod
#     def tearDownClass(self):
#         self.self.driver.close()
#         self.self.driver.quit()
#         print('=====================')
#         print("test Completed")
#         print('=====================')
#
#
# if __name__ == "__main__":
#     unittest.main()
