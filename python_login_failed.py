from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com") #before pre
assert "Swag Labs" in driver.title #ngecheck udah di python org
elem = driver.find_element_by_id("user-name") #object = locator #find_element = selector
elem.send_keys("standard_user")
elem = driver.find_element_by_id("password") 
elem.send_keys("falsepassword")
elem.send_keys(Keys.RETURN)
assert "Epic sadface:" in driver.find_element_by_xpath("//h3[@data-test='error']").text