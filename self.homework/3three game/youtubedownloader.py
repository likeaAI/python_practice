import pytube
from moviepy.editor import *

url = input("다운받을 유튜브주소를 입력 : ")
yt = pytube.YouTube(url)

file_name = yt.title
print(file_name)

#유튜브 객체에서 스트리밍 관련 모든 것 가져오기



#리스트 프린트해주기

#비디오 다운로드(해상도 가장 좋은 것으로 필터)
yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by\
    ('resolution').desc().first().download('D:\DOWNLOAD2\youtube\only video', yt.title)

#오디오 다운로드
yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first()\
    .download('D:\DOWNLOAD2\youtube\only sound', yt.title)




 # 다운받는 파일 경로
videoclip = VideoFileClip("D:\DOWNLOAD2\youtube\only video" , yt.title)
audioclip = AudioFileClip("D:\DOWNLOAD2\youtube\only sound" , yt.title)

# 오디오를 먼저 불러온다.
videoclip.audio = audioclip

# 그 위에 영상을 합쳐서 파일이름으로 저장한다.
# (경로를 지정해줘도 된다. 지정하지 않으면 자동으로 파이썬 파일이 있는 곳에 저장됨)
videoclip.write_videofile(yt.tilte + ".mp4")