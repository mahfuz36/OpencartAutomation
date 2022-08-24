from selenium import webself.drivr
from selenium.webself.drivr.chrome.service import Service
from webself.drivr_manager.chrome import Chromeself.drivrManager
import unittest
import time
from pages.login1_page import LoginPage
from Utils import excel_utils
from selenium.webself.drivr.common.by import By
from selenium.webself.drivr.common.action_chains import ActionChains
from selenium import webself.drivr
from selenium.webself.drivr.support.ui import Webself.driverWait
from selenium.webself.driver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

self.driver = self.self.driver
self.driver.get(self.base_url)
self.driver.maximize_window()
wait = Webself.driverWait(self.driver, 10)

# choose country/region
self.driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li.US a"))).click()

#verify swoosh logo is displayed
logo = self.driver.find_element(By.CSS_SELECTOR, 'span.nsg-glyph--swoosh.gnav-bar--home-logo')
logo.is_displayed()

# open men's hover menu in top nav bar
men_menu = self.driver.find_element_by_css_selector("li[data-nav-tracking=men]")

# click shirt
men_menu.find_element_by_partial_link_text("Shirt").click()

# select a shirt for sale
self.driver.find_element_by_xpath("//div[@id='exp-gridwall-wrapper']/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/div[2]/p").click()

# opening size dropdown
size_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".exp-pdp-size-and-quantity-container a.exp-pdp-size-dropdown")))
actions = ActionChains(self.driver)
actions.move_to_element(size_button).click().perform()

# selecting size
size = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[contains(@class, 'nsg-form--drop-down--option') and normalize-space(.) = 'XL']")))
actions = ActionChains(self.driver)
actions.move_to_element(size).click().perform()

# adding to cart
self.driver.find_element_by_id("buyingtools-add-to-cart-button").click()

# open checkout
checkout_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".checkout-button")))
actions = ActionChains(self.driver)
actions.move_to_element(checkout_button).click().perform()

# select guest checkout
guestlogin_button = wait.until(EC.visibility_of_element_located((By.ID, "ch4_loginGuestBtn")))
actions = ActionChains(self.driver)
actions.move_to_element(guestlogin_button).click().perform()
# self.driver.find_element_by_id("ch4_loginGuestBtn").click()

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

# click next button
self.driver.find_element_by_id("shippingSubmit").click()

# switch to billing frame
wait = Webself.driverWait(self.driver, 10)
self.driver.switch_to.frame("billingFormFrame")

# enter credit card number
cc = wait.until(EC.element_to_be_clickable((By.ID, "creditCardNumber")))
cc.click()
cc.send_keys("4111111111111111")

# enter expiration
selectmonth = Select(self.driver.find_element_by_id("expirationMonth"))
selectmonth.select_by_value("10")

# enter expiration year
selectyear = Select(self.driver.find_element_by_id("expirationYear"))
selectyear.select_by_value("2018")

# enter security code
ccs = self.driver.find_element_by_id("cvNumber")
ccs.send_keys("111")

# enter phone number
phonenum = self.driver.find_element_by_id("phoneNumber")
phonenum.send_keys("5035035033")

# enter email
email = self.driver.find_element_by_id("email")
email.send_keys("test@test.com")

# click submit button
self.driver.find_element_by_id("billingSubmit").click()

# click place order button
self.driver.find_element_by_css_selector("input.ch4_btnOrange").click()

time.sleep(9)
# confirm order was succesful
bodyText = self.driver.find_element_by_tag_name('body').text
self.assertIn("YOUR ORDER WAS PLACED SUCCESSFULLY.", bodyText)
#self.driver.find_element_by_id("ch4_confirmHeading")