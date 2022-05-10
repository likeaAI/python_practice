from selenium import webdriver
from bs4 import BeautifulSoup
import numpy  as np
import pandas as pd
import requests
import re
from time    import sleep ,time
import time as time
from random  import randint

path = 'C:/Users/crid2/driver/chromedriver.exe'
driver = webdriver.Chrome(path)
numbers = range(0,1)
for number in numbers :
    time.sleep(3)
    driver.get('https://www.mk.co.kr/news/stock/?page={}'.format(number))
    main = driver.find_element_by_xpath('//*[@id="container_left"]/div[3]')
    titles =main.find_elements_by_xpath('//*[@id="container_left"]/div[3]/dl[1]/dt/a')


    for title in titles :
        print(title.text)







