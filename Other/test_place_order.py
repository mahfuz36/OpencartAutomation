import unittest
from selenium import webself.drivr
import orders_po
from input_parameters import *
import sys
sys.path.append("tests")


class BuySomething(unittest.TestCase):

    def setUp(self):
        self.self.drivr = webself.drivr.Chrome()
        self.parameters = TestShopParameters
        self.base_url = self.parameters.BASE_URL

    def test_new_order(self):
        self.drivr = self.self.drivr
        self.drivr.get(self.base_url)

        newOrder = orders_po.Order(self.drivr)
        newOrder.shopTShorts()
        newOrder.chooseParticular()
        newOrder.addToCart()
        newOrder.proceedToCheckout()
        newOrder.enterAccount(self.parameters.ORDER_EMAIL, self.parameters.ORDER_PASSWORD)
        newOrder.loginInto()
        newOrder.chooseAddress()
        newOrder.shippingMethod()
        newOrder.paymentMethod()
        newOrder.sendOrder()
        newOrder.checkOrderStatus(self.parameters.ORDER_MESSAGE)

    def tearDown(self):
        self.self.driver.quit()


if __name__ == "__main__":
    unittest.main()