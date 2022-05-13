import csv
from selenium import webdriver
from bs4 import BeautifulSoup
import numpy  as np
import pandas as pd
import requests
import re
from time    import sleep ,time
import time as time
from random  import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



path = 'C:/Users/crid2/driver/chromedriver.exe'
driver = webdriver.Chrome(path)

news_headline = []


numbers = range(1,1000)
for number in numbers :
    time.sleep(4)
    driver.get('https://www.mk.co.kr/news/stock/?page={}'.format(number))

    for i in range(1,26) :
         title = driver.find_element(By.XPATH, '//*[@id="container_left"]/div[3]/dl[{}]/dt/a'.format(i))
         news_headline.append(title.text)


with open('news_headline_total.csv', 'w' , encoding='utf-8') as f :
    writer = csv.writer(f)
    writer.writerow(news_headline)












