# 문자열이 제공하는 함수
# REAL - > 명사적 특징은 -> 변수
           # 동사적 특성은 -> 함수
# *.py 모듈로 본다. (변수와 함수로 이루어짐)
# 인스턴스(프로그램영역 생성된 객체) vs object(실세계 객체)
# 소유의 주체  .  <- 도트
# 클래스란 ? 모든 변수 타입이 객체로 취급됨 , (인스턴스) 객체 생성 템플릿

phoneNumber = "010-4603-2283" #< '-' 기준으로 잘라보고 싶다. 그러면 어떻게 해야할까 ?
print(phoneNumber.split("-")) # 함수의 기능을 말고 문법을 이해 변수.함수() <-

seqText = "Talk is cheap. Show me the code!!" #0은 맨앞 , -1은 맨끝
print('seqText - type, len' , type(seqText), len(seqText) )

# 인덱싱 특정 문자하나를 반환하는 것
print(seqText[0])

# 슬라이싱
print(seqText[0:4]) #simple하게 마지막이 -1이니 내가 1~4자리를 가져오고 싶다면 0~5를 넣어야한다.
print(seqText[-6:0])# 왜 0은 안되지 ?

#[start : end-1 : step]
exStr = "홀짝홀짝홀짝홀짝홀짝홀짝"
# 만약에 홀만 출력하고 싶다면 ?
print(exStr[1::2])
print(exStr[0: len(exStr): 2]) # 굳이 필요없는 방식 전체문자열 반환을 확인하라면 그냥 값을 안넣으면 됨
# 짝수만 나오게함
print(exStr[1::2])
# 홀짝에서 짝홀로 바꾸고 싶다. reverse 끝에서 반대 순서로  출력
print(exStr[::-1]) # reverse 개념


# 문자열 객체가 가지고 있는 함수 소개
strSlicing = 'nice Python'

# 처음 문자를 대문자로 바꾸고 싶다. capitalize
print(strSlicing.capitalize())
# 기존꺼를 - 다른것으로 바꾸고 싶다. replace
print(phoneNumber.replace("-",""))

url = 'http://www.naver.com' # 도메인만 출력하고 싶다.
# find는 index를 반환한다. 즉 위치 그것을 다시 텍스트 반환하는 식으로 구현 가능

print(url[url.find("com"):])

# 다른방법 음 ...
print(url[len(url)-3:])

# 다른방법2
urlList = url.split('.')
#'.' 도트로 문자를 나눈다 함수
print(urlList)
# 리스트 3번째를 출력한다.
print(urlList[2])

# 본인 복습이 젤 중요 강사는 50% 만 가능하다.

companyName = '    samsong     '
print('len - ' , len(companyName))


# 데이터 전처리 방식으로 공백을 날리고 싶다면 ?
print('data  -' , companyName, companyName.strip())
print(len(companyName.strip())) # 7

#전처리 단계에서 대소문자를 하나로 통일 . 아마 upper나 lower 사용 할것같네
print(companyName.upper())
print(companyName.lower())

# mission 1 , 확장자가 xls , xlsx 파일인지 여부를 확인하고 싶다면

fileName = 'report.xls'
print('확장자가 xls , xlsx 파일인지 여부를 확인하고 싶다면- ', fileName.endswith(('xls','xlsx')))
# true 반환 , endwith 특정 문자열을 확인하고 true와 false 반환  # 조건이 2개이기 때문에 튜플형식으로 ('xls'.'xlsx')

# 문자열에 in 연산자를 이용해서 문자열을 판별가능
fruitTxt = 'apple banana pineapple mango grape melon'
print(' in operator -' , 'Apple' in fruitTxt) # false로 반환 apple 은 있지만 Apple은 없다.
print(' in operator -' , 'Apple'.lower() in fruitTxt) #  <- Apple을 lower 을 이용해 apple로 변환

drinking = 'cocacola'
print(len(drinking), drinking.count('c'))  # c라는 문자의 빈도수를 확인 하고 싶다.

# 파일이름이 report 인지를 판단하고 싶다면 ?
print('report 파일인지 여부 -', fileName.startswith('report')) # true 반환



# list ( 중요 )
# not array (배열은 아니다 )
# 순서가 있음 , 중복을 허용한다. , 수정과 삭제가 가능하다.
# index 0부터 시작 ~
# list 선언 방법 2가지  ,1. []  , 2. list() 클래스 선언가능
# 여러개의 스칼라데이터 타입을 담을수있는 변수의 타입

lst = [1,2,3,4 , 'str', ['show', 'me', 'the' , 'code']] # 리스트안에 문자열 뿐만아니라 리스트안에 리스트도 담을수 있다.
# 현업에서 가장 많이 쓰는 방식 [{key:vlaue},{key:vlaue},{key:vlaue}]

print('type - ' , type(lst), lst) # class list 출력 리스트 타입
print('dir - ' , dir(lst)) # 속성확인

# __iter__ 인덱싱과 슬라싱이 가능하다.
print('indexing -' , lst[0]) # list 0번째 (가장첫번째) 값을 반환
print('slicing - ' , lst[0:2])

# list 안에 list를 반환하라면 어떻게 해야할까 ?
print('me - ', lst[-1][1] , type(lst[-1])) # -1 4개가 반환 여기서 다시 0번째 를 반환

# lst[-1][1] -[-1]은 lst의 마지막 값을 반환하고 그다음 [1]은 -1에서 반환되는 리스트의 1값을 반환한다.  트리형 생각하면 될듯
print('slice - ' , lst[-1][1:3])

# 연산가능
x = [1,2,3,4]
y = [4,5]
z = x + y
print(z) # str 을 합치는 개념으로 + 사용됨 , list는 중복이 가능 하기 때문 , 순서도 있고

# 0을 재할당  , list 수정이 가능하다라는 특징 반영
z[0] = 0
print(z)

#list  가지고 있는 함수
z.append(100000) # z에 데이터 항목 추가
print(z)

# insert 와 append 의 차이
z.insert(100,6) # 인서트는 위치까지 지정할수있다. (변수 , 위치 )
print(z)

# 이진탐색이란 ?
# 오름차순
z.sort()
print(z)

# 내림차순
z.reverse()
print(z)

# 데이터를 꺼내는 함수
z.pop(0) # 데이터를 꺼내고 해당 리스트를 인덱스에 있는 값을 삭제한다.
print('pop-' , z)

# 그냥 삭제

del z[0]
print(z)

# remove() z.remove(1) index가 아니라 1값(value)을 삭제한다
# remove del 과 비교


# append() & extend() 비교 **이해 못함 추가 공부해볼것.

lst01 = [1,2,3]
lst02 = [4,5]


# inner list 리스트가 리스트를 포함하는 형태 [ [] , [] ]

inner_lst = [ 'a' , 'b' , 'c'  ]
outer_lst = [10, 3.14 , True , 'string' , inner_lst ] # 숫자 , 실수 , 논리값 , 문자열 , 리스트

print('type - ' , type(inner_lst) , type(outer_lst))
print(outer_lst[-1][0]) # <-- 이해하는거 중요

# range() : 숫자를 순차적으로 생성해주는 객체 , 보통 for와 많이 쓰던데
# 순서를 가지고 있는 스퀀스 타입 , class range , indexing 가능하다는 의미

tmpRange = range(1,11,2) # 11이 아니라 10 이다. range 특성 11  -1 을 빼줘야 된다.  , 1,3,6,9 까지만 표현된것.
print(tmpRange[-1]) # 그리고 마지막값인 9를 반환한다.

# 제어구문, 반복구문
# for ~ in
for idx in tmpRange: # : 블록을 만드는 개념 들여쓰기가 발생한다.
    print(idx, end='\t') # 들여쓰기 구문
# 1 3 5	7 9


import random as r
# 랜덤이라는 모듈을 r이라는 별칭으로 사용하겠다라는 선언
tmpLst = []
for idx in range(5) : # 0~4 까지의 값을 리턴 ( 5개 )
    tmpLst.append(r.randint(1,5))
print('data - ' , tmpLst)

# if ~ in () : 조건 제어
if 4 in tmpLst :
    print(' in ok ')
else :
    print(' not in ')

'''
- list comprehension  ******* 모르는 개념 보강 필요 
- 변수 = [ 실행문  for 변수 in sequence형 객체 ] 
'''

x = [2,4,1,5,3] # 각각의 요소에다가 제곱을 해주고 싶다.

#print(x**2) # 이것이 배열이라면 가능하지만 지금은 리스트기 때문에 제곱이 되지 않는다.
# 루푸를 돌려서 하나씩 제곱한 후 다시 리스트에 넣는 작업으로 완료한다.
result = []
x = [2,4,1,5,3]
for value in x :
    sqrt = value ** 2
    result.append(sqrt)
print(result)

2. # list comprehesion 개념으로 접근하기
result = [value**2 for value in x ] # 위의 포문을 한줄로 줄일수있게 되었다.
print('comprehension -' , result)

'''
튜플 ( tuple ) 
- 선언 : () , tuple() 
- 순서 0 , 중복 허용 , 수정 x , 삭제 x  - immutable 이뮤터블(불변) 객체로 봄
- 읽기 전용 
- indexing, slicing 가능 
- 
'''
tpl = (3,) #(3)일경우 int 형으로 인식한다.
print('type - ' , type(tpl))
print(' indexing slicing - ' , tpl[0] , tpl[0:2], type(tpl[0:2])) # tpl[0]은 int형으로 반환된다.

# tpl[0] = 10  , 튜플은 수정이 되지 않는다.
# TypeError: 'tuple' object does not support item assignment

# 캐스팅(형변환)을 통한 데이터 조작은 가능하다.
lst =list(tpl)
print(type(lst)) # <-list로 변환 , 수정이 가능해진다.

lst[0] : 10
tpl = tuple(lst)
# 다시 list에서 튜플로 변환

#1~99 까지의 정수 중 짝수만 튜플에 저장한다면 ?
# 1. 짝수를 구현하는 법 range(2,100,2)

even_data = tuple(range(2,100,2))
print('type - ' , type(even_data), even_data)


# packing & unpacking **이해가 잘 안됨
packing = ('이지희' , '변윤섭' , '장성원', '정남선' , '노희명' )
x1 , x2 , *x3 , x4 , x5  = packing # unpacking *x3 * 나머지 갯수가 안맞는 것을 리스트로 할당한다.
print('type - ' , type(x1), type(x2), type(x3), x4 , x5)

#  모든 변수를 객체로 취급한다.
# 객체 생성이 가능하다. 이 의미는 객체란 ? 인스턴스 란 변수나 함수를 소유하고 있음







