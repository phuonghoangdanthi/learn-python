from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.set_window_size(700,700)
driver.get('https://www.youtube.com/')
time.sleep(2)

driver.find_element("name",'search_query').send_keys("Don't côi")
driver.find_element("id", 'search-icon-legacy').click()
time.sleep(2)

driver.execute_script('document.querySelector("#video-title > yt-formatted-string").click()')

input()
driver.quit()