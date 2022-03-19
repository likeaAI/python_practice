import os
import glob


files = glob.glob("D:\DOWNLOAD2\youtube\playlist1\*.mp4")
for name in files :
    if not os.path.isdir(name) :
        src = os.path.splitext(name)
        os.rename(name,  src[0]+ '.mp3')