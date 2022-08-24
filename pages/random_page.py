from selenium import webself.drivr
from selenium.webself.drivr import ActionChains
from selenium.webself.driver.chrome.service import Service
from selenium.webself.driver.common.by import By
from webself.driver_manager.chrome import Chromeself.driverManager
import time
from pages.login1_page import LoginPage
from Utils import excel_utils


class LoginPage():

    def tshirt_page(self):
        self.driver = webself.driver.Chrome(service=Service(Chromeself.driverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/index.php")
        # ("http://automationpractice.com/index.php")

        # click shirt
        tshirt_btn = self.driver.find_element(By.XPATH,
                                         "/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[3]/a").click()
        self.driver.implicitly_wait(3)
        quick_view = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/ul/li/div/div[2]/div[3]/ul")
        self.driver.implicitly_wait(3)
        try:
            new_window = ActionChains(self.driver)
            new_window.move_to_element(quick_view).perform()
            time.sleep(3)

            blue_color = self.driver.find_element(By.ID, "color_2").click()
            time.sleep(3)

        except:
            print("Hover not performed")

        add_to_cart = self.driver.find_element(By.XPATH, "//*[@id='add_to_cart']").click()
        self.driver.implicitly_wait(3)
        mass = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[1]/h2')

        mess_verified = mass.is_displayed()
        time.sleep(3)
        if mess_verified is True:
            print('Product successfully added to your shopping cart ')
        else:
            print("No Product Added")
        time.sleep(1)
        # Poceed to checkout
        self.driver.find_element(By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/a').click()
        time.sleep(1)

        # Poceed to checkout-Shopping-cart summary
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/p[2]/a[1]").click()
        time.sleep(1)

        # Poceed to checkout-Addresses
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/form/p/button").click()
        time.sleep(1)
        # Poceed to checkout-Shipping
        self.driver.find_element(By.ID, "cgv").is_selected()
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/form/p/button").click()
        time.sleep(2)

        self.driver.close()


obj = LoginPage()
obj.tshirt_page()
