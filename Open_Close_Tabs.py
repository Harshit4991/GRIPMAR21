#Open and close multiple tabs (10)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path='/home/trainee/Desktop/Automation_Testing/chromedriver')
driver.maximize_window()
time.sleep(0.5)
driver.get('https://google.com/')
time.sleep(0.5)
for i in range(1,10):
    driver.execute_script('window.open('');')
    driver.switch_to.window(driver.window_handles[i])
    driver.get("https://google.com")
    time.sleep(0.5)

for i in range(8,-1,-1):
    driver.close()
    driver.switch_to.window(driver.window_handles[i])
    time.sleep(0.5)

driver.close()
