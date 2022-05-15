
from selenium import webdriver
from selenium.webdriver.common.by import By

import time as time
import csv




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


with open('news_headline_000.csv', 'w' , encoding='utf-8') as f :
    writer = csv.writer(f)
    writer.writerow(news_headline)












