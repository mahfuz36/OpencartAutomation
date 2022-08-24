from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


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
