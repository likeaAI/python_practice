from selenium import webdriver
from bs4 import BeautifulSoup
import numpy  as np
import pandas as pd
import requests
import re
from time   import sleep , time
from random  import randint


path = 'C:/Users/crid2/driver/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=228')

all_news01 = driver.find_element_by_css_selector('ul.type06_headline')
all_news02 = driver.find_element_by_css_selector('ul.type06')
all_link = all_news01.find_elements_by_tag_name('a')
all_link02 = all_news02.find_elements_by_tag_name('a')


for i in range(1,len(all_link),2) :
    link_text = all_link[i].get_attribute('href')
    print()
    print( i-1 ,'번' ,all_link[i].text)
    print(link_text)
    print('*' * 100)
    print()

