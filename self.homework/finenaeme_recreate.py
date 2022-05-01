import os

file_path = 'C:/Users/crid2/OneDrive/바탕 화면/맥주 종류별/상상페일에일'
file_names = os.listdir(file_path)
file_names

i = 1
for name in file_names:
    src = os.path.join(file_path, name)
    dst = 'sangsang' +  str(i) + '.jpg'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1



