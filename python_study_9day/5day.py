# 반복구문

'''
파이썬 반복문 : for ~ , while ~
- break , contunue
- for 변수 in<열거형> :
    <loop body>

-for ~
 else :

- for (초기식 : 조건식 : 증감식) {
    <loop body>
}

초기식선언
- while(조건식) {
    <loop body>
    초기식 증감
    }
'''


# word = 'Beautiful'
# for w in word :
#     print(w , end="\t")
''' 결과
B	e	a	u	t	i	f	u	l	
'''
#
# for w in enumerate(word) :
#     print(w, end="\t")

'''
(0, 'B')	(1, 'e')	(2, 'a')	(3, 'u')	(4, 't')	(5, 'i')	(6, 'f')	(7, 'u')	(8, 'l')
'''
#
# for idx , w in enumerate(word) :
#     print(idx, w, end="\t")


myInfo = {
    'name' : 'seop',
    'Age' : '50',
    'City' : 'Seoul'}

for key in myInfo :
    print(key, end= '\t')
# 키값을 루프돌림 , 이게 싫으면 items ->
for key , value in myInfo.items() :
    print(key, value ,  end='\t')

# break, continue 차이점 확인
'''
- break 특정 조건일때 루프를 빠져나옴
- continue 특정 조건을 만족할때 그 조건 만 빼고 다음 루프를 돌림 , jump 그조건만 실행안하고 루프 이행   
 '''

# break
numbers = [14,3,4,7,10,24,17,2,33,15,34]
for idx, num in enumerate(numbers) :
    if num == 24 :
        print(idx, '- Found!!')
        break
    else :
        print(idx, "- Not Found!!")

# continue



# 파이썬만의 문법 * for ~ in ~ else
'''
전체 루프를 돌리되 else 공통명령문을 실행하고 싶다. 
(보통 if 조건에서는  elif 조건이 여러개 생김 ) 
'''

for number in numbers :
   if number == 0 :
       print("Fonud!!")
       break
else :
    print("Not Found!!")

# 이중 루프구문
# 구구단 2 * (1 ~ 9) , 구구단 3 * (1 ~ 9) ...........



for i in range(2,10) :
    if i == 5 :
        break
    for j in range(1,10) :
        print(f'{i} * {j} = {i*j}' , end = '\t')

# for i, j in range(1,10) : 구현불가 ! , 문법이 허용하지 않는다.
#     gob = i * j
#     print(gob)

# 문자열 처리를 위한 for 구문
str = \
'''
저는 파이썬을 강의중인 강사 임정섭입니다. 
주소는 서울시 입니다. 
나이는 숫자에 불과합니다. 
'''
print(str)
# 문장을 구분하고 단어를  특정 리스트에 담다. ?  hint : for 구문을 이용 , str.split('')
test1 = str.split('\n') # \n 행바꿈 enter 키 역활을 한다.

senten = []
words = []
#******
for s in str.split('\n') :
    senten.append(s)
    for w in s.split() :
        words.append(w)

print('sentences -', senten , len(senten ))
print('words -', words , len(words))

# 연습
apt = [['101호','102호'],['201호','202호'],['301호','302호']]


# 분류 정확도 확인
y_test = [1,0,2,1,0] # 정답
y_pred = [1,0,2,0,0] # 예측값
'''예측값을 정답에 대조하여 다를때 갯수나 확률을 구현'''

for idx in range(len(y_pred)) :
    fit = y_test[idx] == y_pred[idx]
    print(fit)
    acc =+ int(fit) * 20
print('acc -', acc ,'%'  , sep=' ')


#난수 random
import random as r
print('0~1기본적',r.random()) # 기본적으로 실수값을 리턴한다. 세팅없을시
print('1~10사위의 범위',r.randint(1,10))

# 레인지를 list로  바꿔주는 형변환
exdata = list(range(1,10001))
print('dataset -' ,exdata)

# random choices ~

train_data = r.choices(exdata, k=10)
print(train_data)

# while 구문형식
'''
 -  초기식 
-   while (조건식) : 
-   <loop body>
-   증감식
'''
print()
n = 5
while n > 0 :
    print(n)
    n -= 1
# 무한루프 조건이 걸리므로 n을 1씩 감소하여 실행시키게 하였다.
'''
if n ==0 :
    break
'''
lst = ['apple', 'banana', 'mango'] # 데이가 무엇이든 들어가면 boolean은  true 반환
while lst :     # 무한루프가 돌아가버린다. 왜냐면 true 니깐. while true
    print(lst.pop())     # 꺼내면서 비어가면 언젠가는 false로 반환이 된다., 순서가 역순으로 가져옴. get 사용시 인덱스 필요

'''
1 ~ 100 까지의 합, 5의 배수의 합 출력하기
add 3의 배수이면서 5의 배수가 아닌 합을 출력하기
while ~ 구문활용 
'''
#
# cnt = fiveMul = total =  0
# while cnt <= 100 :
#     print(cnt)
#     if cnt % 5 ==0 :
#         fiveMul += cnt
#     cnt += 1
#     if cnt%3 == 0 and cnt %5 != 0 :
#         total += cnt
#     cnt += 1
# print('1~100 사이의 5의 배수의 합 : ' , fiveMul)


#
# #  while ~ else
# lst = ['apple' , 'banana' , 'mango' , 'peer']
# guess = 'peer'
#
# idx = 0
# while idx <len(lst) :
#     if lst[idx] == guess :
#        print("peer 네요 ")
#        break
#     idx += 1  # 맨뒤에 오자 자잘한 에러원인
# else :
#   print("안맞네요")
'''
 - 인자 없고, 리턴 없다.
def a() :
    statement
- 인자 있고, 리턴 없다.
def b(x, y, z) :
    statement
- caller    인자의 개수에 맞게 호출 / 안맞으면 에러
b(10, True, 'Jslim)
- 인자 없고, 리턴 있다.
def c() :
    statement
    returrn value(모든 타입의 변수를 허용)
- caller
  returnValue c()
- 인자 있고, 리턴 있다.

def d(x) :
    statement
    retrun value
- caller
    returnValue =d(10)
'''


def my_sum(x, y, z):  # 인자 3개 리턴도 있는 함수
    sum = x + y + z
    return sum


def print_conins():  # 인자없고 리턴도 없는 함수
    for idx in range(100):
        print('coin ~~ T_T')


def noArgsReturnValue():  # 인자가 없고 리턴이 있는 함수
    return 10, 20


def ArgsNoreturnValue():  # 인자가 있고 리턴이 없는 함수
    print('인자는 있고 리턴이 없다.')


def default_param(x, y, z=True):  # 디폴트 값을 변수 = 값으로 초기에 지정가능하다
    if z:
        data = x * y
    else:
        data = x + y
    return data


# 함수 선언시 가변인수를 정의   '*' ,# 보통 몇개가 들어올지 모를때 루핑작업 ... 등
# *인수 : 튜플 타입으로 봄 , **인수 : 딕셔너리타입을 가변인수로 사용
def argsTuple(*args):
    for idx in range(len(args)):
        print(args[idx], end='\t')
    print()


def kwargsDict(**args):
    for key, value in args.items():
        print('{},{}'.format(key, value))
    print()


def personInfo(*info, **args):  # 뭔가 변형 타입 , 믹스라고 해야할까 .
    weight, height = info
    print(weight)
    print(height)
    for key, value in args.items():
        print('{}{}'.format(key, value))


# mutable(원본에 영향을 미친다. ) - immutable (원본에 영향을 미친다. )
# mutable - List , dict
# immutable - number , str, tuple

def call_by_value(tmp_number):
    tmp_number = tmp_number * 100
    print('inner function -')


def call_by_reference(tmp_number, tmp_list):
    tmp_number = tmp_number + 100
    tmp_list.append(tmp_number)


def userStatistic(func, *data):
    from statistics import mean
    if func == 'sum':
        print(sum(data))
    if func == 'mean':
        print(mean(data))


#
#

# 함수 ! def !
# 내가만든 그리팅 함수 호출
#1
# from study.util.syntax import greeting # study 폴더에서 util 폴더 그다음 syntax 파일 (모듈)에서 greeting함수 호출

#2
#from study.util.syntax import * # 전부 불러오기
from study.util.user_function import * # my_sum , print_coins
result_sum = my_sum(10,20,30) # 리턴을 하는 의미 ?

print('retrun value -' , result_sum)

print_conins() # 함수가 호출되는 시점에서 프린트를 수행한거임 다른변수로 받지 않았기 때문에 호출이 없는 것에 해당
a , b = noArgsReturnValue() # unpacking

print('return tuple -' , a, b)

result = default_param(10,20,0)

argsTuple(1,2,3)
argsTuple(1,2,3,4,5,6)

personInfo(178,96)


#mutable(원본에 영향을 미친다. ) - immutable (원본에 영향을 미친다. )
# mutable - List , dict
# immutable - number , str, tuple

datax = 5
print(call_by_value(datax)) # call by_value 원본에 영향을 미치지 않는다. 값 반환 none 반환됨
print(datax)


# call by refernce
datax = 5
dataL = [10,20]
print(call_by_reference(datax,dataL))
print(datax)

# 함수가 함수를 인자로 받아서 해당 함수를 수행하는 구문
userStatistic('sum' , 1,2,3,4,5,6,7, 8)
userStatistic('mean' , 1,2,3,4,5,6,7, 8)

# 변수의 scope ? ?
# local varible vs global variable
# 함수안에서 쓰는 변수 , 밖에서 쓰는 변수 특징들

# f(X) = y  x값은 함수값이 넣어진상태 입력이 가능하다.

# tmp = 100
# def variableScope() :
    # global local_tmp 를 스면 밖에 변수와 함수안 변수가 같게 된다.
    # 따로 선언이 없으면 다르게 인식한다.
    # 함수는 선언과 초기화가 없으면 문법적 오류가 난다.
#     local_tmp = 0
#     local_tmp += x
#     return local_tmp
#     return tmp
# print(variableScope(tmp))
# print(tmp)

# def my_sqrt(x) :
#     return x**2
#  # map 함수란 ? 함수를 (my_sqrt ,    )  매개변수로 온다.
# lst = map(my_sqrt, range(1,10))
# lst = list(map(my_sqrt , range(1,10)))
# print(lst)
#
# str = list(zip('Hello' , 'Seops', "World"))
# print(str)




# url_list  = makeUrl(lst : list) 반환하고싶다. WWW.GOGLE.COM 앞에 WWW.와 .COM이 뒤에 붙어야 한다.
urls = ['naver', 'gogle', 'samsung']
lst = []


def makeUrl(url) :
    for url in urls :
        sumstring = "www." + url + ".com"
        lst.append(sumstring)
    print(lst)











