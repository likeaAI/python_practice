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
driver.get('https://comic.naver.com/webtoon/weekday')

lists = driver.find_elements_by_class_name('col_inner')
monday_list = lists[0]
link = monday_list.find_elements_by_tag_name('li')

for li in link :
    a_tag = li.find_element_by_tag_name('a')
    href = a_tag.get_attribute('href')


    print(a_tag.text)
    print('link :', href)