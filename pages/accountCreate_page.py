import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class RegistrationPage():
# @pytest.fixture(scope="class")
# class AutoPractice:
    def __int__(self,driver):
        self.driver = driver

    def auto_prac(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://automationpractice.com/index.php")
        # wait=WebDriverWait(driver,10)
        self.driver.maximize_window()
        # request.cls.driver=driver # user the class on test_login
        self.driver.find_element(By.LINK_TEXT, "Sign in").click()
        self.driver.find_element(By.ID, "email_create").send_keys("mahfuzf10@gmail.com")
        self.driver.find_element(By.XPATH, "//*[@id='SubmitCreate']/span").click()
        self.driver.find_element(By.XPATH, "//*[@id='id_gender1']").click()
        self.driver.find_element(By.ID, "customer_firstname").send_keys("Md Mahfuzur")
        self.driver.find_element(By.ID, "customer_lastname").send_keys("Rahman")
        self.driver.find_element(By.ID, "email").is_displayed()
        self.driver.find_element(By.ID, "passwd").send_keys("mahfuz")
        Select(self.driver.find_element(By.ID, "uniform-days")).select_by_index(12)
        Select(self.driver.find_element(By.ID, "uniform-months")).select_by_index(15)
        Select(self.driver.find_element(By.ID, "uniform-years")).select_by_index(1971)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element(By.ID, 'newsletter').click()
        self.driver.find_element(By.ID, "optin").click()
        self.driver.find_element(By.ID, "firstname").send_keys("Md Mahfuzur")
        self.driver.find_element(By.ID, "lastname").send_keys("Rahman")
        self.driver.find_element(By.ID, "company").send_keys("ABC Ltd.")
        self.driver.find_element(By.ID, "address1").send_keys("Dhaka 1207")
        self.driver.find_element(By.ID, "address2").send_keys(" ")
        self.driver.find_element(By.ID, "city").send_keys("Dhaka")
        Select(self.driver.find_element(By.ID, "id_state")).select_by_index(5)
        self.driver.find_element(By.ID, "postcode").send_keys("1207")
        Select(self.driver.find_element(By.ID, "uniform-id_country")).select_by_index(2)
        self.driver.find_element(By.ID, "other").send_keys("ABCDEF")
        self.driver.find_element(By.ID, "phone").send_keys("01758050312")
        self.driver.find_element(By.ID, "phone_mobile").send_keys("01758050312")
        self.driver.find_element(By.ID, "alias").send_keys("DHK")
        self.driver.find_element(By.ID, 'submitAccount').click()
        time.sleep(2)
        self.driver.close()


