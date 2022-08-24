import time
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login_auto_practice(self, email, password):
        email_field = self.driver.find_element(By.ID, "email")
        password_field = self.driver.find_element(By.ID, "passwd")
        signin_button = self.driver.find_element(By.ID, 'SubmitLogin')

        email_field.clear()
        email_field.send_keys(email)
        time.sleep(2)

        password_field.clear()
        password_field.send_keys(password)
        time.sleep(2)

        signin_button.click()



