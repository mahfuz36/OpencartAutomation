from selenium.webdriver.common.by import By

class SignInAndCreate:

    def __init__(self, driver):
        self.driver = driver

    def sign_up(self):
        self.driver.find_element(By.LINK_TEXT, "Sign in").click()

    def enterEmail(self, email):
        # self.driver.find_element(By.LINK_TEXT, "Sign in").click()
        self.driver.find_element(By.ID, "email_create").send_keys(email)
        self.driver.find_element(By.ID, "SubmitCreate").click()

