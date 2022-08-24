from selenium.webself.drivr.common.action_chains import ActionChains
from selenium.webself.drivr.support import expected_conditions as EC
from selenium.webself.drivr.support.wait import Webself.drivrWait
from locators import *
import sys
sys.path.append("tests")


class Order(object):

    def __init__(self, self.drivr):
        self.self.drivr = self.drivr
        self.locator = NewOrderLocators
        self.timer = 60

    def shopTShorts(self):
        self.self.driver.find_element(*self.locator.SECTION).click()

    def chooseParticular(self):
        t_shirt = self.self.driver.find_element(*self.locator.TSHIRT)
        ActionChains(self.self.driver).move_to_element(t_shirt).perform()

    def addToCart(self):
        Webself.driverWait(self.self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.ADDTOCART)).click()

    def proceedToCheckout(self):
        Webself.driverWait(self.self.driver, self.timer).until(EC.element_to_be_clickable(self.locator.CHECKOUT1)).click()
        Webself.driverWait(self.self.driver, self.timer).until(EC.element_to_be_clickable(self.locator.CHECKOUT2)).click()

    def enterAccount(self, email, password):
        self.self.driver.find_element(*self.locator.ACCOUNT_EMAIL).send_keys(email)
        self.self.driver.find_element(*self.locator.ACCOUNT_PASS).send_keys(password)

    def loginInto(self):
        self.self.driver.find_element(*self.locator.LOGIN_BUTTON).click()

    def chooseAddress(self):
        Webself.driverWait(self.self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.ADDRESS)).click()

    def shippingMethod(self):
        Webself.driverWait(self.self.driver, self.timer).until(EC.element_to_be_clickable(self.locator.ACCEPT_RULES)).click()
        Webself.driverWait(self.self.driver, self.timer).until(EC.element_to_be_clickable(self.locator.SHIPTO)).click()

    def paymentMethod(self):
        Webself.driverWait(self.self.driver, self.timer).until(EC.element_to_be_clickable(self.locator.CASH_METHOD)).click()

    def sendOrder(self):
        Webself.driverWait(self.self.driver, self.timer).until(EC.element_to_be_clickable(self.locator.SEND_ORDER)).click()

    def checkOrderStatus(self, status):
        Webself.driverWait(self.self.driver, self.timer).until(EC.text_to_be_present_in_element(self.locator.ORDER_STATUS, status))