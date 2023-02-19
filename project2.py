from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome()
driver.get("https://techwithtim.net")
time.sleep(2)
search = driver.find_element(By.XPATH,'//*[@id="search-2"]/form/label/input')
search.send_keys("Test")
search.send_keys(Keys.RETURN)
time.sleep(2)


input()
driver.quit()
