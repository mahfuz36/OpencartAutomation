from selenium import webself.drivr
import time
from selenium.webself.drivr.common.by import By


class LoginPage():

    def __int__(self, self.drivr):  # constractor
        self.self.drivr = self.drivr

        # Locator
        self.username_textbox_xpath = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        self.password_textbox_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
        self.login_button_xpath = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"

        # test Action

    def enter_username(self, username):
        self.self.drivr.find_element_by_id(self.username_textbox_xpath).clear()
        self.self.drivr.find_element_by_id(self.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.self.drivr.find_element_by_id(self.password_textbox_xpath).clear()
        self.self.driver.find_element_by_id(self.password_textbox_xpath).send_keys(password)

    def click_login(self):
        self.self.driver.find_element_by_id(self.login_button_xpath).click()

    # def login_auto_practice(self,mail,password):
    #     user_mail = self.self.driver.find_element(By.ID,'email')
    #     user_password = self.self.driver.find_element(By.ID,'passwd')
    #     submitLogin_btn = self.self.driver.find_element(By.ID,'SubmitLogin')
    #
    #     user_mail.clear()
    #     user_mail.send_keys(mail)
    #
    #     user_password.clear()
    #     user_password.send_keys(password)
    #     submitLogin_btn.click()
from selenium import webself.driver
from selenium.webself.driver.chrome.service import Service
from webself.driver_manager.chrome import Chromeself.driverManager
import unittest
from pages.Login import LoginPage
#from pages.Login import HomePage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # self.driver = webself.driver.Chrome(executable_path="F:/PeoplenTech QAT
        # Course/Project/MahfuzBITM07/self.drivers/chromeself.driver.exe")
        self.driver = webself.driver.Chrome(service=Service(Chromeself.driverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_login_valid(self):

        self.driver = self.self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login = LoginPage(self.driver)

        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        # homepage = HomePage(self.driver)
        #
        # homepage.click_welcome()
        # homepage.click_logout()

        # regage = RegistrationPage(self.driver)
        # self.self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # self.self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
        # self.self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
        # self.self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        # self.self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").click()
        # self.self.driver.find_element(By.LINK_TEXT, "Logout").click()
        # time.sleep(3)

    @classmethod
    def tearDownClass(self):
        self.self.driver.close()
        self.self.driver.quit()
        print('=====================')
        print("test Completed")
        print('=====================')


if __name__ == "__main__":
    unittest.main()
