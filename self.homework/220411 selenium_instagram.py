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

all_news = driver.find_element_by_css_selector('ul.type06_headline')

link = all_news.find_elements_by_tag_name('a')

print(all_news.text)


for i in range(1,20) :

    print( i ,'번' ,link[i].text)
    print(link[i].get_attribute('href'))
    print('*' * 100)

