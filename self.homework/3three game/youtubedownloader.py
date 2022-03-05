from pytube import YouTube
from pytube import Playlist

DOWNLOAD_FOLDER = "D:\DOWNLOAD2\youtube"
url = "https://www.youtube.com/watch?v=rhWdfjKLrsw"
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


