from bs4 import BeautifulSoup
import urllib.request as req

new = "https://news.daum.net/"
target = req.urlopen(new)
soup = BeautifulSoup(target, "html.parser")

news = soup.select("strong.tit_g") # . 이 class를 의미한다. strong class ="tit_g" = "strong.tit_g"
with open("news.txt" , "w", encoding="utf8") as f:
   for list in news :
      a = list.select_one("a")
      print("링크 : " + a.attrs['href'])
      f.write("링크 : " + a.attrs['href'] + "\n")
      title = a.string.strip() # .strip 공백 제거
      print("제목 : " , title)
      f.write("제목 : " + title + "\n")



