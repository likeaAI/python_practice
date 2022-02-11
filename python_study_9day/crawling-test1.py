import pyinstaller as pyinstaller
from bs4 import BeautifulSoup
import urllib.request as req

# #req.urlopen(웹사이트 주소 ,)
#
# url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
# # url 열기
# result = req.urlopen(url)
# soup = BeautifulSoup(result, "html.parser")
# title = soup.find("title").string
# print(title)
#
# # 실습2
#
# url2 = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"
# target = req.urlopen(url2)
# soup2 = BeautifulSoup(target, "html.parser")
#
# for location in soup.select("location") :
#     print("도시 : " , location.select_one("city").string)
#     print("날씨 : ", location.select_one("wf").string)
#     print("최저기온 : ", location.select_one("tmn").string)
#     print("최고기온 : ", location.select_one("tmx").string)
#     print()

# 실습 3  뉴스기사 크롤링

# 링크 , 제목, 순으로 다음뉴스를 출력할것


file = open("news.txt", "w")

new = "https://news.daum.net/"
target2 = req.urlopen(new)
soup3 = BeautifulSoup(target2, "html.parser")

news = soup3.select("strong.tit_g") # . 이 class를 의미한다. strong class ="tit_g" = "strong.tit_g"
for list in news :
   a = list.select_one("a")
   print("링크 : " + a.attrs['href'])
   file.write("링크 : " + a.attrs['href'] + "\n")
   title = a.string
   print("제목 : " , title)
   file.write("제목 : " + title  + "\n")

file.close()
## none으로 반환되는것까지 a태그를 완전히 제거하지 못함 -> a태그의 부모를 확인
# strong  class=tit_g 클래스를 가짐 이것으로 보다 세세히 분류를 함


