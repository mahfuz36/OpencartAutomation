import unittest
from selenium import webself.drivr
from pages.sign_up_page import SignInAndCreate
from input_parameters import *
import sys
sys.path.append("tests")


class MyStoreRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.parameters = TestRegistrationParameters
        self.base_url = self.parameters.BASE_URL

    def test_base_create_user(self):
        self.driver = self.driver
        self.driver.get(self.base_url)

        baseLogin = SignInAndCreate(driver)
        baseLogin.signIn()
        baseLogin.enterEmail(self.parameters.EMAIL)
        baseLogin.submitEmail()

        baseLogin.addFirstName(self.parameters.FIRST_NAME)
        baseLogin.addLastName(self.parameters.LAST_NAME)
        baseLogin.addPassword(self.parameters.PASSWORD)

        baseLogin.addAddressFirstName(self.parameters.AD_FIRST_NAME)
        baseLogin.addAddressLastName(self.parameters.AD_LAST_NAME)
        baseLogin.addAddress(self.parameters.ADDRESS)
        baseLogin.addAddressCity(self.parameters.AD_CITY)
        baseLogin.selectState(self.parameters.AD_STATE)
        baseLogin.addAddressZipCode(self.parameters.AD_ZIP_CODE)
        baseLogin.selectCountry(self.parameters.AD_COUNTRY)
        baseLogin.addAddressPhone(self.parameters.AD_PHONE)
        baseLogin.addAddressAlias(self.parameters.AD_ALIAS)

        baseLogin.register()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()