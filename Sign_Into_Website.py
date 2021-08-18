#!/usr/bin/env python
# coding: utf-8


#Log in to Mockup website

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path='/home/trainee/Desktop/Automation_Testing/chromedriver')
driver.maximize_window()
driver.get("https://moqups.com/")
time.sleep(3)
sign_in_button=driver.find_element_by_xpath("/html/body/header/nav/div[1]/ul/li[7]/a")
sign_in_button.click()
time.sleep(1)
username=driver.find_element_by_name("email")
username.send_keys("vansh5aron@gmail.com")
password=driver.find_element_by_name("password")
password.send_keys("Mockup@456")
log_in_button=driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div/div[2]/div[2]/form/button")
log_in_button.click()





