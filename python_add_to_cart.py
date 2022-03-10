import unittest
#import page

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Firefox()
# action = ActionChains(driver)

# driver.get("https://www.saucedemo.com") #before pre
# assert "Swag Labs" in driver.title #ngecheck udah di python org
# elem = driver.find_element_by_id("user-name") #object = locator #find_element = selector
# elem.send_keys("standard_user")
# elem = driver.find_element_by_id("password") 
# elem.send_keys("secret_sauce")
# elem.send_keys(Keys.RETURN)

#elem = driver.find_element_by_xpath("//a[@id='item_2_tittle_link']").click()
#elem = driver.find_element_by_link_text("item_2_tittle_link")
#elem.send_keys(Keys.RETURN)

# elem = driver.find_element_by_xpath("//a[@id='item_2_title_link']/div")
# #action.click(elem).perform()
# #action.move_to_element(elem).perform()
# elem.click()

# elem = driver.find_element_by_id("add-to-cart-sauce-labs-onesie")
# elem.click()

#assert "Remove" in driver.find_element_by_id("remove-sauce-labs-onesie") 


class TestRemoveAvailable(unittest.TestCase):

        def setUp(self):
            self.driver = webdriver.Firefox()
            self.driver.get("https://www.saucedemo.com")
            
        def test_remove_available(self):
            elem = self.driver.find_element_by_id("user-name") #object = locator #find_element = selector
            elem.send_keys("standard_user")
            elem = self.driver.find_element_by_id("password") 
            elem.send_keys("secret_sauce")
            elem.send_keys(Keys.RETURN)
            
            elem = self.driver.find_element_by_xpath("//a[@id='item_2_title_link']/div")
            elem.click()
            elem = self.driver.find_element_by_id("add-to-cart-sauce-labs-onesie")
            elem.click()
            element = self.driver.find_element_by_id("remove-sauce-labs-onesie") #mantapmatius
            text = element.get_attribute('innerHTML') #cara dapetinnya check DOM Properties
            assert text == 'Remove',"Remove is visible"
            
if __name__ == "__main__":
    unittest.main()