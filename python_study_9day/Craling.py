import urllib.request

# 다운로드 할 이미지 경로
url = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"

# 저장할 파일 경로 및 이름
imgName = 'C://Users/crid2/PycharmProjects/likeacode/sample1.png'

# 파일 다운로드
# urlretrieve(url, 저장할 파일 경로 )

urllib.request.urlretrieve(url , imgName)
print("저장완료")

# BeautifulSoup

from bs4 import BeautifulSoup

html = """
    <html>
    <head>
        <title>파이썬 웹 크롤링 </title>
    </head>
    <body>
        <h1 id="title">안녕하세요</h1>
        <p id="name">변윤섭입니다</p>
    </body>
    </html>
"""
soup = BeautifulSoup(html ,'html.parser')

h1 = soup.html.body.h1
p = soup.html.body.p

print("h1 :" + h1.string)
print("p : " + p.string)

# find(찾아낼 태그) 함수 , 원하는 태그를 찾아서 반환 , 태그의 이름 속성 속성값
# find all() 전부찾아내서 list로 반환

title = soup.find("h1")
name = soup.find("p")

print("title : " + title.string)
print("name : " + name.string)


html2 = '''
<html>
<head><title>find_all()<title></head>
<body>
    <ul>
        <li>
            <a href = " http://www.naver.com">네이버</a>
        </li>
        <li>
            <a href = " http://www.gogle.com">구글</a>
            
           
        
'''
# 크롤링한 데이터를 for문으로 간략히  표기하는것이 핵심!!
soup = BeautifulSoup(html2, "html.parser")
list = soup.find_all("a")
print(list[0].string)
print(list)
for a in list :
    text = a.string # 이름
    print(text)

for a in list :
    href = a.attrs["href"] # 속성성    print(href)




