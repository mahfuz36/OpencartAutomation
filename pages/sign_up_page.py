from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebdriverWait
from Other.locators import *
import sys


class SignInAndCreate:

    def __init__(self, driver):
        self.driver = driver

    def sign_up(self):
        self.driver.find_element(By.LINK_TEXT, "Sign in").click()

    def enterEmail(self, email):
        self.driver.find_element(By.ID, "email_create").send_key(email)
        self.driver.find_element(By.ID, "SubmitCreate").click()

    # def submitEmail(self):
    #     self.driverWait(self.driver, self.timer).until(
    #         EC.element_to_be_clickable(self.locator.SUBMIT_EMAIL_BUTTON)).click()
    #
    # def addFirstName(self, first_name):
    #     self.driverWait(self.driver, self.timer).until(
    #         EC.element_to_be_clickable(self.locator.FIRST_NAME)).send_keys(first_name)
    #
    # def addLastName(self, last_name):
    #     self.driverWait(self.driver, self.timer).until(
    #         EC.element_to_be_clickable(self.locator.LAST_NAME)).send_keys(last_name)
    #
    # def addPassword(self, password):
    #     self.driverWait(self.driver, self.timer).until(
    #         EC.element_to_be_clickable(self.locator.PASSWORD)).send_keys(password)
    #
    # def addAddressFirstName(self, first_name):
    #     self.driverWait(self.driver, self.timer).until(
    #         EC.element_to_be_clickable(self.locator.ADDRESS_FIRST_NAME)).clear()
    #     self.driverWait(self.driver, self.timer).until(
    #         EC.element_to_be_clickable(self.locator.ADDRESS_FIRST_NAME)).send_keys(first_name)
    #
    # def addAddressLastName(self, last_name):
    #     self.driverWait(self.driver, self.timer).until(
    #         EC.element_to_be_clickable(self.locator.ADDRESS_LAST_NAME)).clear()
    #     self.driverWait(self.driver, self.timer).until(
    #         EC.element_to_be_clickable(self.locator.ADDRESS_LAST_NAME)).send_keys(last_name)
    #
    # def addAddress(self, address):
    #     self.driverWait(self.driver, self.timer).until(
    #         EC.element_to_be_clickable(self.locator.ADDRESS)).send_keys(address)
    #
    # def addAddressCity(self, city):
    #     self.driverWait(self.driver, self.timer).until(
    #         EC.element_to_be_clickable(self.locator.ADDRESS_CITY)).send_keys(city)
    #
    # def selectState(self, state):
    #     try:
    #         element = self.driverWait(self.driver, self.timer).until(
    #             EC.presence_of_element_located(self.locator.ADDRESS_STATE))
    #
    #     finally:
    #         select_state = Select(element)
    #         select_state.select_by_visible_text(state)
    #
    # def addAddressZipCode(self, zip_code):
    #     self.driverWait(self.driver, self.timer).until(
    #         EC.element_to_be_clickable(self.locator.ADDRESS_ZIP_CODE)).send_keys(zip_code)
    #
    # def selectCountry(self, country):
    #     try:
    #         element = self.driverWait(self.driver, self.timer).until(
    #             EC.presence_of_element_located(self.locator.ADDRESS_COUNTRY))
    #
    #     finally:
    #         select_country = Select(element)
    #         select_country.select_by_visible_text(country)
    #
    # def addAddressPhone(self, phone_number):
    #     self.driverWait(self.driver, self.timer).until(
    #         EC.element_to_be_clickable(self.locator.ADDRESS_PHONE_NUMBER)).send_keys(phone_number)
    #
    # def addAddressAlias(self, alias):
    #     self.driverWait(self.driver, self.timer).until(
    #         EC.element_to_be_clickable(self.locator.ADDRESS_ALIAS)).clear()
    #     self.driverWait(self.driver, self.timer).until(
    #         EC.element_to_be_clickable(self.locator.ADDRESS_ALIAS)).send_keys(alias)
    #
    # def register(self):
    #     self.driverWait(self.driver, self.timer).until(
    #         EC.element_to_be_clickable(self.locator.REGISTER_BUTTON)).click()
    #
    # def driverWait(self, driver, timer):
    #     pass
