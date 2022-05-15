from _xxsubinterpreters import get_current

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time as time
import csv




path = 'C:/Users/crid2/driver/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://en.dict.naver.com/#/main')

text_word = ['apple' , 'have']
mean_words = []

for word in text_word :
    search_input = driver.find_element(By.XPATH, '//*[@id="ac_input"]')
    search_input.send_keys(word)
    time.sleep(1)
    search_input.send_keys(Keys.RETURN)
    time.sleep(1)

    ### 현재 url 다시 드라이브에 get 해서 다음으로 넘어갈수있게 함

    driver.get(driver.current_url)
    time.sleep(1)
    search_output = driver.find_element(By.XPATH, '//*[@id="searchPage_entry"]/div/div[1]')
    time.sleep(1)
    mean_words.append(search_output.text)
    print(search_output.text)

    # 그다음 url 가져오고 다시 돌아가기
    time.sleep(1)
    driver.get('https://en.dict.naver.com/#/main')


print(mean_words)









#
# numbers = range(1,1000)
# for number in numbers :
#     time.sleep(4)
#     driver.get('https://en.dict.naver.com/#/main')
#
#
#
#     for i in range(1,26) :
#          title = driver.find_element(By.XPATH, '//*[@id="container_left"]/div[3]/dl[{}]/dt/a'.format(i))
#          news_headline.append(title.text)
#
#
# with open('news_headline_000.csv', 'w' , encoding='utf-8') as f :
#     writer = csv.writer(f)
#     writer.writerow(news_headline)
#
#
#









