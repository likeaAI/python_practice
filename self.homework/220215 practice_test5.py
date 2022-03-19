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

# 파이썬문법 print end옵션이 관건이다.  end옵션은 그뒤의 출력값이 이어서 출력한다.
# or 구문으로 돌려도 연달아 연결할수있다는 의미 (사실 이게 효율적인지는 잘 모르겠다만 )
for t in range(10 ) :
    a =  2t+ 3
    print(type(a), a * '!')