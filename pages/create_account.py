import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class NewAccount:

    def __init__(self, driver):
        self.driver = driver

    def create_account(self, firstname,lastname,email,password,company,address,city,state,zip,country,mobilephone):

        # filling out order form
        firstname = self.driver.find_element_by_id("fname")
        firstname.click()
        firstname.clear()
        firstname.send_keys("testname")
        firstname.send_keys(Keys.TAB)

        lastname = self.driver.find_element_by_id("lname")
        lastname.send_keys("testname")
        lastname.send_keys(Keys.TAB)

        address = self.driver.find_element_by_id("address1Field")
        address.send_keys("test address")
        address.send_keys(Keys.TAB)

        city = self.driver.find_element_by_id("singleCity")
        city.send_keys("testcity")
        city.send_keys(Keys.TAB)

        state = self.driver.find_element_by_id("singleState")
        state.send_keys("Oregon")
        state.send_keys(Keys.TAB)

        postalcode = self.driver.find_element_by_id("postalCodeField")
        postalcode.send_keys("97202")
        postalcode.send_keys(Keys.TAB)
