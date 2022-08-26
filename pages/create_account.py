import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

#
# class NewAccount:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def create_account(self, firstname,lastname,email,password,company,address,city,state,zip,country,mobilephone):
#
#         # filling out order form
#         firstname = self.driver.find_element_by_id("fname")
#         firstname.click()
#         firstname.clear()
#         firstname.send_keys("testname")
#         firstname.send_keys(Keys.TAB)
#
#         lastname = self.driver.find_element_by_id("lname")
#         lastname.send_keys("testname")
#         lastname.send_keys(Keys.TAB)
#
#         address = self.driver.find_element_by_id("address1Field")
#         address.send_keys("test address")
#         address.send_keys(Keys.TAB)
#
#         city = self.driver.find_element_by_id("singleCity")
#         city.send_keys("testcity")
#         city.send_keys(Keys.TAB)
#
#         state = self.driver.find_element_by_id("singleState")
#         state.send_keys("Oregon")
#         state.send_keys(Keys.TAB)
#
#         postalcode = self.driver.find_element_by_id("postalCodeField")
#         postalcode.send_keys("97202")
#         postalcode.send_keys(Keys.TAB)


from Utils.param import RegistrationPageLocators

from locators.registrationpagelocators import RegistrationPageLocators
from selenium.webdriver.support.ui import Select
import time


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class AccountRegistrationPage(BasePage):

    def fill_in_account_registration_form(self):
        time.sleep(5)
        firstnam_element = self.driver.find_element(*RegistrationPageLocators.FIRSTNAME_TEXT_INPUT)
        firstnam_element.send_keys('firstname')
        lastname_element = self.driver.find_element(*RegistrationPageLocators.LASTNAME_TEX_INPUT)
        lastname_element.send_keys('lastname')
        password_element = self.driver.find_element(*RegistrationPageLocators.PASSWORD_TEXT_INPUT)
        password_element.send_keys('password')
        address_element = self.driver.find_element(*RegistrationPageLocators.ADDRESS_TEXT_INPUT)
        address_element.send_keys('address')
        city_element = self.driver.find_element(*RegistrationPageLocators.CITY_TEXT_INPUT)
        city_element.send_keys('city')
        states_dropdown_element = self.driver.find_element(*RegistrationPageLocators.STATE_DROPDOWN)
        states_dropdown_element.click()

        state_select = Select(self.driver.find_element(*RegistrationPageLocators.STATE_DROPDOWN))
        state_select.select_by_visible_text('Alaska')

        postal_code_element = self.driver.find_element(*RegistrationPageLocators.POSTAL_CODE_TEXT_INPUT)
        postal_code_element.send_keys('12345')
        phone_element = self.driver.find_element(*RegistrationPageLocators.PHONE_NUMBER_TEXT_INPUT)
        phone_element.send_keys('123456789')
        alias_element = self.driver.find_element(*RegistrationPageLocators.ALIAS_TEXT_INPUT)
        alias_element.clear()
        alias_element.send_keys('testalias')

    def click_regiser_button(self):
        register_button_element = self.driver.find_element(*RegistrationPageLocators.REGISTER_ACCOUNT_BUTTON)
        register_button_element.click()

    def get_page_title(self):
        return self.driver.title
