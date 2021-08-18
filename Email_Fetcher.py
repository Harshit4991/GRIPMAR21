#!/usr/bin/env python
# coding: utf-8



#Extract emails from the links fetched through google results
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import csv
import re

df=pd.read_csv("Final_Output.csv")

driver=webdriver.Chrome(executable_path="/home/trainee/Desktop/Automation_Testing/chromedriver")
driver.maximize_window()
list1=[]
for i in range(len(df)//25):
    print(df["Corresponding URLs"][i])
    link=df["Corresponding URLs"][i]
    driver.get(link)
    doc=driver.page_source
#     emails=re.findall(r'[\w\.-]+@[\w\.-]+', doc)
    emails=re.findall('([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', doc)
    for e in emails:
        print(e)
        list1.append(e)
    time.sleep(3)

driver.close()
print(list1)
de_duplicator=set(list1)
print(de_duplicator)
list1=list(de_duplicator)
print(list1)




