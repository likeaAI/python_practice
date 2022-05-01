import os
import glob


files = glob.glob("C://Users//crid2//Downloads//강한 IPA//*.*")


for name in files :
    if not os.path.isdir(name) :
        src = os.path.splitext(name)
        os.rename(name,  src[0] + '.jpg')