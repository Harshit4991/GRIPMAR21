from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time

driver=webdriver.Chrome(executable_path="/home/trainee/Desktop/Automation_Testing/chromedriver")

driver.maximize_window()
driver.get("https://www.google.com/")

search=driver.find_element_by_name("q")
search.send_keys("ToXSL")

time.sleep(1)

button=driver.find_element_by_name("btnK")
button.click()
