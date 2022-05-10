import os
import glob


files = glob.glob("C://Users//crid2//ml-data//beertest03//all_beer01//구스아일랜드//*.*")


for name in files :
    if not os.path.isdir(name) :
        src = os.path.splitext(name)
        os.rename(name,  src[0] + '.png')