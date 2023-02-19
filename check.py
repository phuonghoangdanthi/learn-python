from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="chromedriver")
#initialize web driver
with webdriver.Chrome(service=service) as driver:
    #navigate to the url
    driver.get('https://pythonexamples.org/')
    time.sleep(2)
    #find element that has link text : 'OpenCV'
    my_div = driver.find_element(By.LINK_TEXT,'openCV').click()
    time.sleep(2)
    #press on browser's back button 
    #driver.back()
input()
driver.quit()
