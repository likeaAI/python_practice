from bs4 import BeautifulSoup
import requests
import re

response = requests.get('https://en.wikipedia.org/wiki/List_of_American_exchange-traded_funds')
print('response -' ,response.text)
soup = BeautifulSoup(response.text , 'html')
print('type - ' , type(soup))

