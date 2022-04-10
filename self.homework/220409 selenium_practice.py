from selenium import webdriver
from bs4 import BeautifulSoup
import numpy  as np
import pandas as pd
import requests
import re
from time    import sleep , time
from random  import randint



# 일동제약 홈페이지에서 셀레늄으로 상품 웹크롤링을 해보자.
# 크롬 세팅
path = 'C:/Users/crid2/driver/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://www.ildong.com/kor/product/list.id?page=1&halt=&prdDisease=&prdCategory=&searchVal=&searchOption=0')

for page in range(1, 3):
    print('page - ', page)
    driver.get('https://www.ildong.com/kor/product/list.id?page=' + str(
        page) + '&halt=&prdDisease=&prdCategory=&searchVal=&searchOption=0')
    sleep(3)

    list = driver.find_element_by_class_name('prList')  # <div class='prlist' >
    a_tags = list.find_elements_by_tag_name('a')

    # print( len(a_tags) )
    data = []

    for idx in range(len(a_tags)):
        a_tags[idx].click() # 각 제품링크 href 를 클릭을 의미
        detail = driver.find_element_by_class_name('detailCnt2')
        detail2 = driver.find_element_by_class_name('detailCnt1')


        data.append(detail2.text)
        data.append(detail.text)
        data.append('*' * 100)
        # print(detail2.text)
        # print(detail.text)
        # print('*' * 100)
        sleep(2)

        driver.back()

        list = driver.find_element_by_class_name('prList')
        a_tags = list.find_elements_by_tag_name('a')


print(data)