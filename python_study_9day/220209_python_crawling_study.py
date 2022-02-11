

from bs4 import BeautifulSoup
import urllib.request as req

# #req.urlopen(웹사이트 주소 ,)

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
# url 열기
result = req.urlopen(url)
soup = BeautifulSoup(result, "html.parser")
title = soup.find("title").string
print(title)

# 실습2

url2 = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"
target = req.urlopen(url2)
soup2 = BeautifulSoup(target, "html.parser")

for location in soup.select("location") :
    print("도시 : " , location.select_one("city").string)
    print("날씨 : ", location.select_one("wf").string)
    print("최저기온 : ", location.select_one("tmn").string)
    print("최고기온 : ", location.select_one("tmx").string)
    print()


with open("data/wether.txt", "w", encoding="utf8") as f:
    for location in soup.select("location") :
        f.write("도시 : " + location.select_one("city").string + "\n")
        f.write("날씨 : " + location.select_one("wf").string + "\n")
        f.write("최저기온 : " + location.select_one("tmn").string + "\n")
        f.write("최고기온 : " +  location.select_one("tmx").string + "\n" + "\n" + "\n")








