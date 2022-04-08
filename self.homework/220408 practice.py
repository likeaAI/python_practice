import numpy  as np
import pandas as pd
from bs4 import BeautifulSoup
import urlopen
import requests
import re

url = 'https://comic.naver.com/index'
webtoon = requests.get(url)
soup = BeautifulSoup(webtoon.text , 'lxml')


lists = soup.find_all('div' > 'li', attrs={'class' : 'asideBoxRank'} )

url2 = 'https://movie.daum.net/ranking/boxoffice/weekly'
daum_movie = requests.get(url2)
soup2 = BeautifulSoup(daum_movie.text , 'lxml')


daum_movie_list = []
daum_movie_open = []
movie_lists = soup2.select(' .tit_item a')
for movie in movie_lists :
   daum_movie_list.append(movie.get_text())

open_date = soup2.select( '.txt_num')
for date in open_date :
   daum_movie_open.append(date.get_text())



daum_report = pd.DataFrame({'open' : daum_movie_open , 'title' : daum_movie_list})
daum_report['ranking'] = [i for i in range(1,16)]
daum_report.index = daum_report['ranking']
daum_report.drop('ranking' , axis=1)
print(daum_report)
