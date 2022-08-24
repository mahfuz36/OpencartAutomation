from selenium.webself.driver.self.common.by import By


class NewOrderLocators(object):
    SECTION = (By.CSS_SELECTOR, "#block_top_menu > ul > li:nth-child(3) > a")
    TSHIRT = (By.XPATH, '//*[@id="center_column"]/ul/li/div/div[1]/div/a[1]/img')
    ADDTOCART = (By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/div[2]/a[1]')
    CHECKOUT1 = (By.CSS_SELECTOR, "#layer_cart > div.clearfix > div.layer_cart_cart.col-xs-12.col-md-6 > div.button-container > a")
    CHECKOUT2 = (By.XPATH, '//*[@id="center_column"]/p[2]/a[1]')
    ACCOUNT_EMAIL = (By.ID, "email")
    ACCOUNT_PASS = (By.ID, "passwd")
    LOGIN_BUTTON = (By.ID, "SubmitLogin")
    ADDRESS = (By.XPATH, '//*[@id="center_column"]/form/p/button')
    ACCEPT_RULES = (By.XPATH, '//*[@id="form"]/div/p[2]/label')
    SHIPTO = (By.XPATH, '//*[@id="form"]/p/button')
    CASH_METHOD = (By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a')
    SEND_ORDER = (By.XPATH, '//*[@id="cart_navigation"]/button')
    ORDER_STATUS = (By.XPATH, '//*[@id="center_column"]/p[1]')


class CreateAccountLocators(object):
    SIGN_IN_BUTTON = (By.CLASS_NAME, "login")
    ENTER_EMAIL = (By.ID, "email_create")
    SUBMIT_EMAIL_BUTTON = (By.ID, "SubmitCreate")
    FIRST_NAME = (By.ID, "customer_firstname")
    LAST_NAME = (By.ID, "customer_lastname")
    PASSWORD = (By.ID, "passwd")
    ADDRESS_FIRST_NAME = (By.ID, "firstname")
    ADDRESS_LAST_NAME = (By.ID, "lastname")
    ADDRESS = (By.ID, "address1")
    ADDRESS_CITY = (By.ID, "city")
    ADDRESS_STATE = (By.ID, "id_state")
    ADDRESS_ZIP_CODE = (By.ID, "postcode")
    ADDRESS_COUNTRY = (By.ID, "id_country")
    ADDRESS_PHONE_NUMBER = (By.ID, "phone_mobile")
    ADDRESS_ALIAS = (By.ID, "alias")
    REGISTER_BUTTON = (By.ID, "submitAccount")