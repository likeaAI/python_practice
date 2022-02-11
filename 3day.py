'''
 python 범용적으로쓰는 딕셔너리 타입을 알아보는 시간
 list 안에 dict를 많이 쓴다. [{key : value}]
 선언 : {key : value } , dict() # sequence 타입이 아니다 , 맵핑이기 때문에 인덱싱 슬라이싱 문법은 적용되지 않는다.
 특징 1. 순서가 없음, 2. 키 중복을 허용하지 않는다. 3. 수정은 가능  4. 삭제 가능
 '''

tmpDict = {
    'name' : 'jslim' ,
    'phone' : '01046032283' ,
    'birth' : '730910'
}
print('type -' , type(tmpDict), tmpDict) # 반환값 type - <class 'dict'>

'''
동적으로 데이터를 담는다  -> 비어있는 딕셔너리를 만들고 프로그램이 수행할때 담아주는 방식을 많이 쓰게 될것이다. 
한마디로 처음부터 데이터가 완전히 정해진 경우는 거의 없다.
'''

# in 연산자를 이용해 key 중복을 유무를 확인할수 있다.
print('key 검사 -' , 'name' in tmpDict) # true 반환

tmpDict = {
    '메로나' : [300,20] ,
    '비비빅' : [400,20] ,
    '죠스바' : [100,50]
}
# 딕셔너리 값을 꺼낼때 키값으로 꺼낼수 있다.

# if 메로나의 가격정보를 확인하고 싶다면 ?
print(tmpDict['메로나'])
# [300, 20 ] , 리스트 타입으로 반환되었다. 인덱싱과 슬라이싱이 가능하다.
print(tmpDict['메로나'][0],'원')
print('메로나의 가격은 {}원이다., 메로나의 수량은 {}개입니다. '.format(tmpDict['메로나'][0] , tmpDict['메로나'][1]))

# 메로나의 가격은 300원이다., 메로나의 수량은 20개입니다.

# 기존 딕셔너리에  새로운 데이터를 만약 새롭게 추가 하고 싶다면 ?
tmpDict['메로나'] = [500,50]
print(tmpDict) # 메로나 가격이 수정됨 , 에러가 날것같은데 안남, 중복된 키값은은 에러가 아니라 수정을 해버림 **

# 메로나의 가격을 인상해보고 싶다. 10% 인상하고자 한다면 ?
melon_list = tmpDict['메로나'] # 메로나 [500,50] list 소환 0
melon_list[0] = melon_list[0] * 1.1 # 재할당
print(tmpDict)
'''
딕셔너리 타입에서 리스트 타입을 호출한다. 리스트 타입 전체 계산은 어렵기 때문에 [0] 하나의 객체를 소환해서
그 값을 원하는 값을 연산한다. 
그 후에 재할당을 하여 출력하면 원하는 값이 나온다. 
'''

tmpDict = {
    'name' : '섭섭해' ,
    'City' : 'Seoul' ,
    'Age' : 50 ,
    'Grade ' : 'A+' ,
    'Status' : True
}
# 딕셔너리 value 값은 어떤타입이든 들어갈수 있다.
tmpDict['name'] = '임정섭' # 바로 키값에 접근해 수정할수 있다.
print(tmpDict)

tmpDict = dict([
    ('city' ,'seoull') ,('age', 50)
])
print('type - ' , type(tmpDict), tmpDict)

# 함수 dict()을 선언할경우 튜플로 키와 벨류를 한쌍으로 표현해야한다.  -> dict( [ ( key  , value  ) ] )
tmpDict = dict([('city' , 'seoul') , ('Age' , 50)])
print(tmpDict)

# get 의 사용 법
print(tmpDict.get('city'))  # 오류가 발생하면 none 값을 반환 오류를 발생시키지는 않는다.

#  새로운 데이터를 추가 하고 싶다. ? , 해당키가 존재한다면 중복된다면 수정이되고 , 없다면 추가가 될것이다.  ?
#** 보강할것.


# zip 흐트러진 자료를 하나의 딕셔너리로 만들어 준다.
keys = ('apple' , 'pear' , ' peach')
values = (1000 , 1500 , 2000)

 # type - <class 'zip'> <zip object at 0x0000018413A91B80> < ?? 객체의 주소번지가 반환됨
 # 형변환을 하면 해결이된다. 형변환 ?

#1 FOR 문으로 구현
'''
zipDict = {}
for idx in range(len(keys)) :
    zipDict[keys[idx]] = values[idx]
'''

# #2
# zipDict =(zip(keys,values))
# print(dict(zipDict)) # zip을 쓸대 앞에 dict()해줘야 정상적으로 값이 반환됨


# 일반적으로 dict 순서가 x for loop문을 쓰기에는 무리가 있음 다른방법으로 반복해야된다.
# dict - keys() , values() , items() 각각 함수 사용법 확인

zipDict = {}
for key in zipDict.keys():
    print('{} : {}'.format(key, zipDict.get(key)))
#
# for values in zipDict.values():
#     print(values)
#
# #** item 은 딕타입의 키와 벨류값을 모두 반환시키는 함수이다.
# for values in zipDict.items():
#     print('{} : {}'.format(keys, values))

#
# # dict () 내용을 한번에 지우는 기능
# zipDict.clear()
# print(zipDict)

# # pop()
# print('pop -' , zipDict.pop('apple'))

'''
set 집합의 자료형, 사용빈도는 높지는 않음 
- 선언 : {} , set()
- 순서x   , 중복 x  , 유니크한 값을 확인해볼때 사용됨
- i ,s x   
 '''

# tmpSet = {1,2,3,4,5,6,7,1,1,2,2,5}
tmpSet = set([5,4,3,2,1,1,2,3,4,5,6,7,1,1,2,2,5]) # list 안에 중복데이터를 한번씩만 출력한다. 중복 x
print('type - ' , type(tmpSet) , tmpSet) # 중복값을 표현하지 않는다.

tmpT = tuple(tmpSet) # 데이터 타입을 SET -> TUPLE 변환
print(tmpT)

tmpL = list(tmpSet)
print(tmpL)

gender = ['남' , '남' , '여' , '남' , '남' , '여' , '남' , '남' , '여' ]
test1 = set(gender)
print(test1) # 중복 제거용 사용하면 좋을것같다.

# set도 요소를 추가할수있다. , 중복된 데이터는 추가되지 않는다. (오류가 발생하지 않는다. )

set01 = set('life is mine')
print(set01) # 중복된값을 모두 날리고 각각 객체만 표현해준다 공백제외

# intersection - 교집합
set02 = set([1,2,3,4,5])
set03 = set([6,7,3,4,5])

print(set02.intersection(set03)) # 교집합
print(set02.union(set03)) # 합집합
print('difference 차집합 ', set02.difference(set03))

set02.add(9) # 하나의 인자만 추가할수있다. ([10,11]) add 는 불구하다. 그럼 update를 써서 2개이상 인자를 추가 , 안에 리스트화 필수
print(set02)
set02.update([10,11])
print(set02)

set02.clear()
print(set02)

'''
boolean Type  참과 거짓을 반환한다.
 - True | False
 - 논리연산자(not ,and ,or ) 
 - 비교연ㅅ나자( ~ , & , | )
 - "" , [] , {} ,  , 0 , none -> False
'''
# print(bool(-1))  - > True  ,# print(bool(0))  - > False

'''
날짜 특정패키지 모듈 
'''
from datetime import date, datetime , timedelta
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse

# relativedelta -> year, month
# timedelta -> week, day, hour, minute , second



# 날짜끼리 계산을 할수있는가.
today = date.today()
# day = timedelta(days=-1)
day = relativedelta(months= -2)
print(type(today),today, today+day)

# 문자열로 표현된 날짜를 계산가능 ?
myDate = parse("2022-01-27")
print('type - ' , type(myDate) ,  myDate)

# 날짜타입 문자열 포맷으로 지정 할 수 있다. %m , %d, %y , %h %m %s
print('format - ' , myDate.strftime("%m-%d-%y"))
print('format - ' , myDate.strftime("%m-%d-%Y")) # (날짜 데이타)를 문자열로 바꿔준다.


str = '2019-12-25'
print(type(str))
print('문자 -> 날짜 - ', datetime.strptime(str,'%Y-%m-%d'))


'''
사용자 입력 
input 
bool 은 타입을 input 입력하면 뭘 입력해도 True 반환한다. 
이거 왜이럼   ? 
'''

