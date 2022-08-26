import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class RegistrationPage():
#     def __int__(self,driver):
#         self.driver = driver

    def auto_prac(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("http://automationpractice.com/index.php")
        # wait=WebDriverWait(driver,10)
        driver.maximize_window()
        # request.cls.driver=driver # user the class on test_login
        driver.find_element(By.LINK_TEXT, "Sign in").click()
        driver.find_element(By.ID, "email_create").send_keys("mah311@gmail.com")
        driver.find_element(By.XPATH, "//*[@id='SubmitCreate']/span").click()
        time.sleep(1)
        gender = driver.find_element(By.XPATH, "//*[@id='id_gender1']")
        gender_status = gender.is_selected()
        if not gender_status:
            gender.click()
        time.sleep(1)

        driver.find_element(By.ID, "customer_firstname").send_keys("Md Mahfuzur")
        driver.find_element(By.ID, "customer_lastname").send_keys("Rahman")
        driver.find_element(By.ID, "email").is_displayed()
        driver.find_element(By.ID, "passwd").send_keys("mahfuz")
        Select(driver.find_element(By.ID, "uniform-days")).select_by_index(12)
        Select(driver.find_element(By.ID, "uniform-months")).select_by_index(15)
        Select(driver.find_element(By.ID, "uniform-years")).select_by_index(1971)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        driver.find_element(By.ID, 'newsletter').click()
        driver.find_element(By.ID, "optin").click()
        driver.find_element(By.ID, "firstname").send_keys("Md Mahfuzur")
        driver.find_element(By.ID, "lastname").send_keys("Rahman")
        driver.find_element(By.ID, "company").send_keys("ABC Ltd.")
        driver.find_element(By.ID, "address1").send_keys("Dhaka 1207")
        driver.find_element(By.ID, "address2").send_keys(" ")
        driver.find_element(By.ID, "city").send_keys("Dhaka")
        Select(driver.find_element(By.ID, "id_state")).select_by_index(5)
        driver.find_element(By.ID, "postcode").send_keys("1207")
        Select(driver.find_element(By.ID, "uniform-id_country")).select_by_index(2)
        driver.find_element(By.ID, "other").send_keys("ABCDEF")
        driver.find_element(By.ID, "phone").send_keys("01758050312")
        driver.find_element(By.ID, "phone_mobile").send_keys("01758050312")
        driver.find_element(By.ID, "alias").send_keys("DHK")
        driver.find_element(By.ID, 'submitAccount').click()
        time.sleep(2)
        driver.close()

obj = RegistrationPage()
obj.auto_prac()

# import unittest
# import time
# from pages.signin_page import SignIn
# from pages.newAccount import CreateAccountPage
# from Utils.param import Configuration
# from pages.sign_up_page import SignInAndCreate
# from pages.newAccount import  CreateAccountPage
#
#
# class SignInTest(unittest.TestCase):
    # def test_signin(self):
    #     global driver
    #     baseUrl ="http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creationp"
    #     driver = Configuration.BROWSER
    #     # driver.implicitly_wait(5)
    #     driver.get(baseUrl)
    #     time.sleep(2)
    #
    #     signup = SignInAndCreate(driver)
    #     signup.sign_up()
    #     signup.enterEmail("maf0034@gmail.com")
    #     time.sleep(2)
    #
    #     ta = CreateAccountPage(driver)
    #     ta.create_account('Mr.','firstName','lastName','password','address','city','postalCode','phone','aliasAdress','state')
    #
    #     # ta = CreateAccountPage(driver)
    #     # # ta.select_gender()
    #     # ta.setFirstName("Kamal")
    #     # ta.setLastName("Jaml")
    #     # ta.setPassword("123456")
    #     # ta.setAddress("address")
    #     # ta.setCity("city")
    #     # ta.setPostalCode("12070")
    #     # ta.setPhone("123456789")
    #     # ta.setAliasAdress("AliasAdress")
    #     # ta.selectState()
    #     # ta.clickRegister()






