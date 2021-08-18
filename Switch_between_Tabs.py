#Switch between tabs

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path='/home/trainee/Desktop/Automation_Testing/chromedriver')
driver.maximize_window()
time.sleep(0.5)
driver.get("https://www.touropia.com/best-places-to-visit-in-serbia/")
time.sleep(1)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.thecrazytourist.com/15-best-places-visit-serbia/")
print(driver.title)
print(driver.current_url)
driver.close()
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
driver.close()





