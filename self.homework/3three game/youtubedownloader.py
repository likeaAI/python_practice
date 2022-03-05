import pytube
from moviepy.editor import *
from pytube import Playlist
import time


print("다운로드 유형을 고르세요 ")
print("1번 영상 하나 url 타입  ")
print("2번 영상 하나 플레이리스트 타입  ")

main = int(input())
if main == 1 :

    url = input("다운받을 유튜브주소를 입력 : ")
    yt = pytube.YouTube(url)

    file_name = yt.title
    print(file_name)
    print("길이 : ", yt.length)
    print("게시자 : ", yt.author)
    print("게시날짜 : ", yt.publish_date)
    print("조회수 : ", yt.views)
    print("키워드 : ", yt.keywords)
    print("설명 : ", yt.description)
    print("썸네일 : ", yt.thumbnail_url)

    #비디오 다운로드(해상도 가장 좋은 것으로 필터)
    yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by\
        ('resolution').desc().first().download('D:\DOWNLOAD2\youtube\only_video', yt.title[0:4])
    #오디오 다운로드
    yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first()\
        .download('D:\DOWNLOAD2\youtube\only_sound', yt.title[0:4])
     # 다운받는 파일 경로
    videoclip = VideoFileClip("D:\\DOWNLOAD2\\youtube\\only_video\\" + yt.title[0:4])
    audioclip = AudioFileClip("D:\\DOWNLOAD2\\youtube\\only_sound\\" + yt.title[0:4])
    # 오디오를 먼저 불러온다.
    videoclip.audio = audioclip
    # 그 위에 영상을 합쳐서 파일이름으로 저장한다.
    # (경로를 지정해줘도 된다. 지정하지 않으면 자동으로 파이썬 파일이 있는 곳에 저장됨)
    videoclip.write_videofile("D:\\DOWNLOAD2\\youtube\\" + yt.title[0:4] +".mp4")


else :

    url2 = input("다운받을  플레이리스트 주소를 복사해서 넣어보자. :  ")
    p2 = Playlist(url2)
    for video in p2.videos:

        video.streams.filter(adaptive=True, file_extension='mp3', only_audio=True).order_by('abr').desc().first() \
            .download('D:\DOWNLOAD2\youtube\downloadmusic')

