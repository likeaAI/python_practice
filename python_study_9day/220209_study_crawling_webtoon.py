import requests
from bs4 import BeautifulSoup
naverwebtoon = "https://comic.naver.com/webtoon/weekday"

# 네이버 웹툰 크롤링 해보기
# 네이버 와 통신 확인 -

respones = requests.get(naverwebtoon)
print(respones.status_code) # 200 반환 통신 문제없음

# 네이버 웹툰 크롤링 준비 1 분류하기
soup = BeautifulSoup(respones.text, "lxml")
#print(soup) 가져와짐 그냥 html.persal 사용 네이버웹툰서버에서  끊어버림 , html안되면 텍스트를 가져와서 할것.

# 그닥 좋은방버은 아닌데
uploads = soup.select("ol > li > a" )
for i in range(1,10) :
    print(i , "위")
    print("링크 " + "https://comic.naver.com/"+uploads[i].attrs['href'])
    print("제목" + uploads[i].string)












