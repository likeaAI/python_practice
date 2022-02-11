# print
# sep option ,
print('P','Y','T','H','O','N')
print('P','Y','T','H','O','N', sep='')
print('010', '4683', '2283', sep='-')
print('jslim9413', 'naver.com', sep=('@'))
# end 옵션
# end option(println() - print() ) 끝에서 연결 그래서 end

print('Welcome TO')
print('Seop Wordl')

# 위2개구문을 한줄로 출력하고 싶다.
print('Welcome TO', end='')
print('Seop Wordl')
# println() <-현재 없기 때문에 라이브러리 로 다운받아서 쓰던지
# format 옵션 을 사용법 (%d,%s,%f) 정수, 문자열 ,
print('섭섭해님의 나이는 : {} 성별은 : {}'.format(50,"여"))
# 그냥하면 왼쪽부터 오름차순 0,1, 순으로 할당
print('섭섭해님의 나이는 : {1} 성별은 : {0}'.format(50,"여"))
# 0,1으로 순서를 지정해줄수있다.
#자릿수 지정 가능 !
print('섭섭해님의 나이는 : %d 이고 성별 %s 입니다.'%(50, "남"))
print('%5s' % ('python study' , )) # 5자리할당이지만 글자가 넘어가도 전부출력
print('%.5s' % ('python study' , )) #. 절삭 글자가 넘어가면 출력안됨
# %d 10진 정수사용 ,#s 글자를 의미 ,
print('%d %d' % (1, 2))

# %f 실수(소수 자리 ) 6자리가지 출력가능
print('%f' % (3.14159250))
print('%f' % (3.14159252))
print('%1.2f' % (3.1415925)) #1.2 1에서 둘째자리 소수점가지 구현

# 변수 ?
''' python Bulit-in types 
- Numberic 
- Sequence 
- Text Sequence
- Set
- Bool
'''
# 파이썬에는 배열 (인공지능 툴에서 보통 많이 쓰는 ) numpy ndarray 타입이 존재하지 않는다.

# 변수를 선언하는 다양한 방법 ? (변수란 데이터를 담는 그릇으로 이해 )
'''
- camel case  : numberOfCollegeGraduates # 처음에 소문자로 구분 하여 대문  
- pascal case : NumberOfCollegeGrauates # 처음에 대문자로 소문자로 하여 구문 
- snake case  :  _ 언더바로 구분 
'''

# 변수는 숫자로 시작할수 없고, 특수문자 _ , $ 만 허용이됨.
# 대소문자를 구분한다.
# 변수를 ,로 이용해서 변수를 열거할수없다. ex) age =10 , AGE = 20 XXX
# 파이썬에 기본 내장은 변수로 사용불가
# 예약어는 사용불가

# pirnt('변수' -')
age = 10
Age = 20
print(age, Age, type(age) , type(Age))

# import keyword <- keyword 모듈
# keyword.py
# keyword.함수() , keyword.변수

import keyword
kw = keyword.kwlist
# ** 중요한 버릇 변수의 타입을 확인하는 버릇을 들여야한다. !
print(type(kw))

# 리스트 타입
test1 = [1, 2, 3, 4, 5, 6, 7, "coffee"]
print(type(test1))

# 변수 바인딩 ( = 연사자 이용해서 할당) , 오른쪽에 있는 데이터를 왼쪽으로 할당
year = '2022'
month = '1'
day = '25'

print('{}년 {}월 {}일 입니다. '.format(year,month,day))
print(f'{year}년 {month}월 {day}일 입니다.')

intValue =123
floatValue = 3.14
boolValue = True  # 소문자 true  인식 안됨  , | <- or 을 의미
strValue = 'jimsim'

# boolvalue 타입
# 변수에 데이터가 있으면 True -> 그것을 int 1  반환 가능 반대로 false , 0으로 반환 가능
name =''
print('type - ',(type(intValue) , type(floatValue) , type(strValue)))
print(int(bool(name) ), type(int(bool(name))))
# list 스칼라타입( 단일타입)을 담을수있는 list = []

test3 = []
print(type(test3))

# 딕셔너리 타입 (key, value ) type
dict = { "name" : "machineLearning" , "version" : 2.0 }
print(type(dict))

# 인공지능에서 가장 많이 사용하는 타입 lsit -> 배열 변경후 사용

tuple = (3)
# 인수가 한개일경우 튜플형식이 아니라 인수형식으로 반환함
# tuple(3, )   , 로 해결
print("type - ", type(tuple))

# dict 타입에 키를 주지 않는 값은 set 타입이라고 부른다.
set1 = {3,5,7}
print(type(set1))

str01 = " I am Python"
str02 = 'I am Python'
str03 = '''
this is a
multi line comment'''
print(type(str01), type(str02), type(str03))
print(str03)