#!/usr/bin/env python
# coding: utf-8



#import pandas as pd
#df=pd.read_csv("Search_Phrases.csv")
#df["Search Strings"][0]



#Search string, fetch URLs from search results, copy them into csv file
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import pandas as pd
from pandas import DataFrame

df=pd.read_csv("Search_Phrases.csv")

def ultra_fxn(data):
    df2=pd.read_csv("Final_Output.csv")
    driver=webdriver.Chrome(executable_path="/home/trainee/Desktop/Automation_Testing/chromedriver")

    driver.maximize_window()
    driver.get("https://www.google.com/")
    
    search=driver.find_element_by_name("q")
    search.send_keys(data)
    
    time.sleep(1)
    search.submit()
    
    all_elements = []
    phrase=[]
    for num in range(5):
        for element in driver.find_elements_by_xpath('//div[@class="tF2Cxc"]'):
            link=element.find_element_by_xpath('.//div[@class="yuRUbf"]/a').get_attribute('href')
            print(link)
            all_elements.append(link)
            
        time.sleep(2)
        
        if num==4:
            break
        else:
            next_button=driver.find_element_by_link_text("Next")
            next_button.click()
            
    phrase=[data for i in range(len(all_elements))]
        
#     print(all_elements)
#     print(phrase)
    
    df3=pd.DataFrame(list(zip(phrase, all_elements)),columns=['Searched String', 'Corresponding URLs'])
    df2=pd.concat([df2,df3], ignore_index=False)
    print(df2)
    
    df2.to_csv("Final_Output.csv", index=False)
    time.sleep(2)
    driver.close()


for k in range(len(df)):
    ultra_fxn(df["Search Strings"][k])
    



#Get all links on a webpage
# elems = driver.find_elements_by_xpath("//a[@href]")
# for elem in elems:
#     print(elem.get_attribute("href"))




#import pandas as pd
#df2=pd.read_csv("Final_Output.csv")
#df_empty=df2[0:0]
#df2=df_empty
#df2.to_csv("Final_Output.csv", index=False)
#df2









