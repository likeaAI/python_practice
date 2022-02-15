# 이중루프를 이용하여 삼각형을 출력하라


for i in range(11) :
     tree = '*'
     print(i * tree)

#2
# for j in range(1,12) :
#     three2 = '*'
#     starnumber = int( 2j + 1)
#     print( starnumber * three2)

for y in range(1,11 ) :
    for s in range(10 - y):
        print(' ' , end = '')
    for x in range(y*2 - 1 ) :
        print('*', end= '')
    print(' ')