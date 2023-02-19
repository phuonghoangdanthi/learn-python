from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/")
"""driver.find_element(By.LINK_TEXT, "Courses").send_keys(Keys.ENTER)
time.sleep(5)
input()
driver.close()
"""

menu = driver.find_element(By.CSS_SELECTOR,".nav")
hidden_submenu = driver.find_element(By.CSS_SELECTOR,".nav # submenu1") 
actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(hidden_submenu)
actions.perform()
time.sleep(5)
input()
driver.close()