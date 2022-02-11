


# 제어문 반복문
'''
제어구문 - if
if 논리값 :
    True 일경우 statement (문장) 을 수행한다.
else :
    statment

True : 0이아닌 수 , 문자, 또는 데이터 있는 리스트 튜플 집합 딕셔너리  <-- 파이썬만이 갖는 특성
False : 0 , '', 데이터가 없는 리스트 튜플 집합 딕셔너리
'''
#
# tmpStr ='' # 리스트가 비어있으면 false
#
# if tmpStr :
#     print('true block')
# else :
#     print('false block')
#
#
# tmpStr2 ='life is mine' # 리스트가 있으면 true
#
# if tmpStr2 :
#     print('true block')
# else :
#     print('false block')
#
# tmpStr3 = 0 #0은 false, 나머지는 true 취급
#
# if tmpStr3 :
#     print('true block')
# else :
#     print('false block')
# #---------------------------------------------------
#
# score = int(input("점수입력 : "))
# if score >= 60 :
#     print('pass')
# else :
#     print('fail')

# 파이썬만의 특성  if ~ in
area = {'서울' : 100, '부산': 150, '대전':200}
region = '부산'
if region in area :
    print('키 값이 존재합니다. key-', region)
else :
    print('{}지역은 포함되지 않습니다.'.format(region))

'''
윤년의 조건 
'''
year = 2022
if (year%4 == 0  and year%100 != 0) or year%400 == 0  :   # != 아니거나 not equal
    print('leap year')
else :
    print('year')


# # 중첩 구문
# lst31 = [1,3,5,7,8,10,12]
# if month != 2 :  # 2가 아니다 부정표현
#     if month in lst31 : # if in~ if 안에 if 구문
#         pass
#     else :
#         pass
# else :
#     if :
#         pass
#     else :

# 다중 조건문 , elif

'''
100 ~ 85 :'우수' , 84~70 : '보통' , 69이하 : '저조'
'''

# 3항 연산자
# 변수 = '참' , if(조건식) else '거짓'
num =  9
three_caul = num *2 if num >=5 else num + 2 # 3항 연산자 , 쉼표가 없다.
print(three_caul)

# 예제1
tmpDict = {
    'name' : 'jslim' , 'city' : 'seoul', 'grade' : 'A'
}
print('in - ', 'name' not in tmpDict) # 키로 검색함 tmpDict.keys() 동일 기능
print('in - ', 'jslim' in tmpDict) # 벨류로 검색함 tmpDict.values() 동일 기능

'''
관계 연산자 
 > , <  , =  , >= , <= , == , !=
 
 산술 > 관계 > 논리 순서로 적용
'''


test1 = 5+10 > 3 and 7+3 == 10
print(test1)
test2 = 5+10 > 3 and not 7+3 == 10
print(test2)

id01 = 'vip'
id02 = 'admin'
grade = 'platinum'

if id01 == 'vip' or id02 == 'adimin' :
    print('관리자 인증')
if id02 == 'admin' and grade == 'platinum' :
    print('최상위 관리자 인증')


'''
파이썬 반복문 for ~ , while 
- for 변수 in <열거형> : <- 리스트 튜플 등만 들어갈수있다.
    <loop body>  
파이썬만 특징 
for ~ 
else :
- for (초기식 : 조건식 : 증감식 ) {
<loop body>
}
'''
#
# scores = []
# for i in range(5):
#     scores.append(int(input("성적을 입력해주세요 : ") ) )
# print(scores)
#
# for idx in range(len(scores)) :
#     print((scores[idx]) , '\t' , end = " ")
#
# calcu =  0
# for calcu in scores :
#     calcu += scores
# print(scores)


# while 무한루프 방법2가지 하나는 whilte true <- false 로 변환 하던지 break 를 걸던지
# 올림픽은 4년마다 개최 , 2000 ~ 2050 사이의 올림픽이 개최되는 년도를 출력하시오
# 한줄에 5개의 년도씩 출력
# print(end = )

# cnt = 0
# for year in range(2000,2050, 4) :
#     cnt += 1
#     if cnt%5 == 0 :
#         print(year , end='\n')
#     else :
#         print(year, end='\t')
#
#
# tmpLst = [1,2,3,4,5,6,7,8,9] # 2의 배수만 제곱하고 싶다. , 나머지 2로 나눈 나머지가 == 0 일때 그값만 제곱해주는 식
#
# newLst = [i**2 for i in tmpLst if i%2 ==0]
#
# # for i in tmpLst :
#     if i%2 == 0 :
#         newLst.append( i**2)
#

# 세 글자 이상인 문자만 출력 ?
# tmplst = ['I' , 'am' , 'studying' , 'PYTHON' , 'language' , '!!']
# lst = [data for data in tmplst if len(data) >=3 ]
# print(lst)

# lst = []
# for data in tmplst :
#     if len(data) >=3 :
#         lst.append(data)
# print(lst)
#
# # 대문자만 출력하고 싶다. isupper()
# lst = []
# for i in tmplst :
#     if i.isupper() :
#         lst.append(i)
# print(lst)


# 확장자를 제외한 파일 이름만 출력해보고 싶다.  split
tmpLst = ['gretting.py' , 'ex01.py' , 'intro.hwp' , 'bigdata.doc', 'machine_learnig.jupyer']
lst = []
for idx in range(len(tmpLst)) :
    print(tmpLst[idx].split(".")[0])



