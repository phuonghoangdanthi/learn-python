from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.set_window_size(700,700)
driver.get('https://pythonexamples.org/')
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="menu-top-menu"]/li[3]/a').click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
#driver.refresh()

input()
driver.quit()