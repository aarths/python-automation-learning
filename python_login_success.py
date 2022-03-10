from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com") #before pre
assert "Swag Labs" in driver.title #ngecheck udah di python org
elem = driver.find_element_by_id("user-name") #object = locator #find_element = selector
elem.send_keys("standard_user")
elem = driver.find_element_by_id("password") 
elem.send_keys("secret_sauce")
import time 
time.sleep(3)

elem.send_keys(Keys.RETURN)
