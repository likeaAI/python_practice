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
lists_01 = soup.select(' .asideBoxRank')


print(lists_01)
webtoon_list = []
for list in range(len(lists_01)) :
    webtoon_list.append(lists_01[list].get_text())

print(webtoon_list)

