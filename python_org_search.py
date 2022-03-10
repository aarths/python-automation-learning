from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org") #before pre
assert "Python" in driver.title #ngecheck udah di python org
elem = driver.find_element_by_id("id-search-field") #object = locator #find_element = selector
elem.send_keys("wakwaw")
import time 
time.sleep(3)
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source