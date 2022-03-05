from pytube import YouTube
from pytube import Playlist
DOWNLOAD_FOLDER = "D:\DOWNLOAD2\youtube"

print("다운로드 유형을 고르세요 ")
print("1번 영상 하나 url 타입  ")
print("2번 영상 하나 플레이리스트 타입  ")

main = int(input())
if main == 1 :
        url = input("다운받을 주소를 복사해서 넣어보자. :  ")
        yt = YouTube(url)

        stream = yt.streams.get_highest_resolution()
        stream.download(DOWNLOAD_FOLDER)


        print("제목 : ", yt.title)
        print("길이 : ", yt.length)
        print("게시자 : ", yt.author)
        print("게시날짜 : ", yt.publish_date)
        print("조회수 : ", yt.views)
        print("키워드 : ", yt.keywords)
        print("설명 : ", yt.description)
        print("썸네일 : ", yt.thumbnail_url)


else :
    inputplay = input("플레이스 리스트 주소를 복사해서 넣어라 ")
    p = Playlist(inputplay)
    for video in p.videos:
        video.streams.first().download(DOWNLOAD_FOLDER)




