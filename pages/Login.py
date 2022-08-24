
class LoginPage():

    def __int__(self, self.drivr):  # constractor
        self.self.drivr = self.drivr

        # Locator
        self.signin_link_xpath = "/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a"
        self.email_textbox_xpath = '//*[@id="email"]'
        self.password_textbox_xpath = '//*[@id="passwd"]'
        self.login_button_xpath = '//*[@id="SubmitLogin"]'
        # test Action

    # def click_sign(self):
    #     self.self.drivr.find_element_by_xpath(self.signin_link_xpath).click()
    #
    # def enter_email(self, email):
    #     self.find_element_by_xpath(self.email_textbox_xpath).clear()
    #     self.find_element_by_xpath(self.email_textbox_xpath).send_keys(email)
    #
    # def enter_password(self, password):
    #     self.find_element_by_xpath(self.password_textbox_xpath).clear()
    #     self.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)
    #
    # def click_login(self):
    #     self.find_element_by_xpath(self.login_button_xpath).click()

    def login_auto_practice(self, email, password):
        self.find_element_by_xpath(self.signin_link_xpath).click()

        self.find_element_by_xpath(self.email_textbox_xpath).clear()
        self.find_element_by_xpath(self.email_textbox_xpath).send_keys(email)

        self.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

        self.find_element_by_xpath(self.login_button_xpath).click()
        print(login_button_xpath)    
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


