from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get("https://www.cermati.com/app/gabung")
time.sleep(10) #waiting pop up notification

elem = driver.find_element(By.ID, 'email')
elem.send_keys("Aa_Automation@gmail.com")

elem = driver.find_element(By.ID, 'mobilePhone')
elem.send_keys("081234567890")

elem = driver.find_element(By.ID, 'password')
elem.send_keys("KataSand1")

elem = driver.find_element(By.ID, 'confirmPassword')
elem.send_keys("KataSand1")

elem = driver.find_element(By.ID, 'firstName')
elem.send_keys("Technical")

elem = driver.find_element(By.ID, 'lastName')
elem.send_keys("Test")

elem = driver.find_element(By.ID, 'cityAndProvince')
elem.send_keys("denpasar")
time.sleep(5) #waiting dropdown field ready
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.XPATH, '//*[@data-button-name="register-new"]')
elem.click()
time.sleep(30)
