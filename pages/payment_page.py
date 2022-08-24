import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class PaymentShoping:

    def __init__(self, driver):
        self.driver = driver

    def payment_page(self):

        # PLEASE CHOOSE YOUR PAYMENT METHOD
        self.driver.find_element(By.LINK_TEXT, "Pay by check.").click()
        time.sleep(2)

        # ORDER SUMMARY
        confirm_order = self.driver.find_element(By.XPATH,'//*[@id="cart_navigation"]/button').click()
        time.sleep(2)




