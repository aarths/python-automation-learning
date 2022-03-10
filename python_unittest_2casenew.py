#TEST DRIVEN DEVELOPMENT TEST

import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class TestCheckout(unittest.TestCase):
	def setUp(self):
		self.driver= webdriver.Firefox()
		self.driver.get("https://www.saucedemo.com")
		login = self.driver.find_element_by_id("user-name")
		login.send_keys("standard_user")
		login = self.driver.find_element_by_id("password")
		login.send_keys("secret_sauce")
		login.send_keys(Keys.RETURN)

	def test_1_icon_available(self):
		elem = self.driver.find_element_by_id("add-to-cart-sauce-labs-onesie")
		elem.click() 
		assert "1" in self.driver.find_element_by_class_name("shopping_cart_link").text
		self.driver.close()


	def test_2_field_validation(self): #test_2 untuk order execution
		elem = self.driver.find_element_by_id("add-to-cart-sauce-labs-onesie") #kenapa harus ngulangin? bisa ga ngelanjutin?
		elem.click() 
		elem = self.driver.find_element_by_class_name("shopping_cart_link")
		elem.click()
		elem = self.driver.find_element_by_id("checkout")
		elem.click()
		elem = self.driver.find_element_by_id("first-name")
		elem.send_keys("Ayip")
		elem = self.driver.find_element_by_id("last-name")
		elem.send_keys("IsInTheHouse")
		elem = self.driver.find_element_by_id("continue")
		elem.click() 
		assert "Error: Postal Code is required" in self.driver.find_element_by_xpath("//h3[@data-test='error']").text

if __name__ == "__main__":
    unittest.main()
    setUp(test_icon_available)