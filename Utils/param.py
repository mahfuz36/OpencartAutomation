from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class TestRegistrationParameters(object):
    BASE_URL = "http://automationpractice.com/index.php"
    EMAIL = "email@emaillcc.com"
    FIRST_NAME = "Name"
    LAST_NAME = "Family"
    PASSWORD = "password"
    AD_FIRST_NAME = "Name"
    AD_LAST_NAME = "Family"
    ADDRESS = "New Avenue 35-2"
    AD_CITY = "Tallinn"
    AD_STATE = "Arizona"
    AD_ZIP_CODE = "33454"
    AD_COUNTRY = "United States"
    AD_PHONE = "53444443"
    AD_ALIAS = "test"


class Configuration(object):
    BASE_URL = "http://automationpractice.com/index.php"

    BROWSER = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # ORDER_EMAIL = "email@emailll.com"
    # ORDER_PASSWORD = "password"
    # ORDER_MESSAGE = "Your order on My Store is complete.


class CreateAccountLocator:
    MrTitle_id = 'id_gender1'
    firstName_id = 'customer_firstname'
    lastName_id = 'customer_lastname'
    password_id = 'passwd'
    days_id = 'days'
    months_id = 'months'
    years_id = 'years'
    address_id = 'address1'
    city_id = 'city'
    state_id = 'id_state'
    postalCode_id = 'postcode'
    country_id = 'id_country'
    phone_id = 'phone_mobile'
    aliasAdress_id = 'alias'
    register_id = 'submitAccount'
    logout_xpath = '//a[@title="Log me out"]'

