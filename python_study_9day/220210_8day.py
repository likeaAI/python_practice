'''
학습목표
- 예외처리
- 매직함수, 데코레이터, 제너레이터 , 일급함수
- 파일 입출력
'''


# 예외처리 - ex) int형만 입력하는 란에 str입력해서 에러가 난다면 ...
'''
Exception - XXXXError , value , index보다 상위로 Exception에러로 걸고하면 다 제외처리가 잘된다. 
 예외처리 구문 
 try : 
    예외가 발생 할 가능성이 있는 코드를 정의 하는 곳 
 except A : 
    발생한 예외를 잡기 위한 객체를 정의하고 처리하는 곳
 except B : 
    발생한 예외를 잡기 위한 객체를 정의하고 처리하는 곳
 else   :
    예외가 발생되지 않을 때 실행되는 곳 
 finally :  
    정상 , 비정상 상관없이 무조건 수행되는 곳 
    
 '''

# function define - worker
def smpInput() :
    try :  # 단독 실행이 불가 쌍을 이뤄야 함 Try :  ~ except a :
        age = int(input('나이를 숫자로 입력해 주세요  :  '))
        print('your age is ' , age, ' years old')
    except ValueError as e :
        print(str(e))

# else 의 모순 , try가 작동하지 않으면 정상코드가 실행되는데 그걸 굳이 else로 다시 정의할필요가 잇을까?
def smpInput2() :
    try :  # 단독 실행이 불가 쌍을 이뤄야 함 Try :  ~ except a :
        age = int(input('나이를 숫자로 입력해 주세요  :  '))

    except ValueError as e :
        print(str(e))
        smpInput() # 재귀 호출 : 오류가 나면 정상입력할때가지 입력란을 재 출(함수로)

    else :
        print('your age is ', age, ' years old')


# caller
# else
# smpInput2()
# print("programing end - ")

'''
매개 변수로 넘겨 받은  각 첨자 번지의 값에 제곱한 결과를 출력하려고 한다.
예외 발생을 확인하고 예외처리 구문을 추가하여 정상적인 흐름의 함수 호출이 되도록 만들어 본다면 ? 
'''

#리스트 제곱하는 법
# test2 = [ 2,4,6,]
# for i in test2 :
#     sqrt = i**2
#     print(sqrt)

def exceptionFunc(lst) :

        for e in lst :
            try:
                print('raw -', e)
                sqrt = e**2
                print('squared -' , sqrt)
            except TypeError as e:
                pass
# try가 for 밖에 있느냐 안에 있느냐에 따라서 결과과 다르게 나온다. 그것을 이해해보자.
# try가 for 밖에 있으면 한번 에러가 생겼을때 except로 넘어가서 중단이 된다.
# for 안이라면 에러가 생겨도 다시 for문으로 돌아가서 재실행하기 때문에 'num'을 제외한 나머지가 출력된다.
# caller
usrlsr = [10,20,25,'num' ,40 ,50]
# exceptionFunc(usrlsr)

# 정상인데 예외로 만든다면 ?
# 사용자 정의 예외클래스를 만들 수 있다.

class UserNegativeDivisionError(Exception) :  # 인위적으로 예외처리를 하고싶은 구문
    def __init__(self,msg) :
        self.msg = msg


def positiveDivide(x , y) :
    if (y  <  0) :
        raise UserNegativeDivisionError('음수로 나눌 수 없습니다.')
    else :
        return x/y

try :
    result = positiveDivide(10, -1 )
    print(' call positive func - ' , result)
except UserNegativeDivisionError as e :
    print(e.msg)
except ZeroDivisionError as e :
    print(e.args[0])
print('progoramming end - ')

# 예외에 처리하는 문법에 대한 이해가 필요하다. 예외 오류를 미리 예측하기는 힘들다.
# 특정 조건을 예외를 일으킬수있어야한다.


# magic function __xxxx__() 알고있어야하는거 몇가지
class MagicClass(object) :
    def __init__(self):
        print('객체 생성시 호출 ')
    def __del__(self):
        print('객체 삭제시 호출 ')
    def __str__(self):
        return('이제는 주소값이 아니라 문자열이 출력')


obj = MagicClass() # 매직함수 리스트
print('dor - ' , dir(obj))
print(obj) # obj.__str__() 오버라이딩 해서 원하는 문자열로 리턴시켜준다. 생략되어있음
            # 주소값이 직히면 문자열로 오버라이딩해서 다시 사용하자.

# 알면 좋은 매직함수
'''
__repr__
__str__

'''


# 일급함수, 일급 클래스 ? first class ? 프로그램 유연성 확대 목적 ( 꼭 알아야되는건 아님)
# - 변수에 함수를 저장할 수 있다.
# - 함수를 다른 함수의 인자로 전달할수 있다.

def userAdd(x,y ):
    return x + y

print('add - ' , userAdd(10,20))
print('function address - ', userAdd) # 함수를 변수처럼 넣을 수 있을까 ?
# -> <function userAdd at 0x000002C2DA2DAD40> 함수의 호출로 표현이 된다.
f = userAdd # 기존 함수를 변수에 할당했다.
print('f - add -' , f(10,20)) # 함수를 변수에 저장
                            # 이게 무슨의미일까 ? 함수만 할당한다. 기존함수에 들어간 ()값들은 상관없다.


# 파이썬에서 모든것은 객체로 될수있다.

# 함수를 다른 함수의 인자로 전달
def userOperation(func, arg ) :
    func(arg[0] ,arg[1])

data = (10,20)
result = userOperation(userAdd, data)
print('result add-' , result)

# 함수의 리턴값으로 다른 함수를 사용할 수 있다.
# closure (함수 내부에 자료구조를 생성하여 값을 저장해 놓는 개념)
def outter(x) :
    def inner(y) :
        return x + y
    return inner  # outter 에 대한 리턴 , 보통 변수(value ) 리턴값을 줬는데 함수에 리턴값을 줘버리는 경우
# caller
# inner() 함수안에 함수 접근불가
result = outter(5)

# generator ? : 반복문 ?
# - 장점 : 빠른 수행속도 , 적은 메모리 사용으로 인한 성능향상 ,쉽게 생각하면 for loop 구문

def loopFunc(lst) :
    result2 =[]
    for tmp in lst :
        result2.append(tmp**2)
    return result2

#caller
data = [1,2,3,4,5]
result2 = loopFunc(data)
print('result -' , result2)

def generatorFunc(lst) :
    for tmp in lst :
        yield tmp**2

#caller
result3 = generatorFunc(data)
print('generator type- ' , type(result3))
print('next -' , next(result3)) # 첫번째 값이 리턴
print('next -' , next(result3)) # 두번재 값이 리턴
print('next -' , next(result3))
print('next -' , next(result3))

# 리턴하지 않았는데 리턴값을 받았다라... / 루핑을 컨트롤 할수있다.
# 대용량의 데이터 적은양의 메모리를 필요한 요소를 한줄씩 가져올수 있다.
# ex) 10만건의 데이터를 for loop 쓰면 오래걸리니 건바이건으로 표현할수있다.

# list 컴프레이션 활용
lst = [tmp ** 2 for tmp in data]
generator = (tmp **2 for tmp in data )
print('type - ' , generator)

for g in generator :
    print(g)
print("end for ~ ")
for g in generator :
    print(g)
# 출력을 다하면 문자열이 반환 , 무한히 반복되지는 않는다.
print('end for ~ ')
print('generator -' , list(generator))

# 파일 입출력
'''
- open(file = xxx , mode = "r|w|a" , encoding =xxxxx )
- with open() as file  :
'''
# pandas 기반 입출력

# def readText(path, mode ) :
#     file = None
#     try :
#         file = open(path, mode , encoding='utf-8')
#         print('file type - ' , type(file) , file)
#         print('read -' , file.read())
#     except Exception as e :
#         print(str(e))
#     else :
#         print('read - "\n' , file.read())
#     finally:
#         if file != None : # file open 하는 시점에서 에러 코드를 견고하게 만들기 위해서 넣음
#             file.close()

#caller
# readText('./data/greeting.txt' , "r")
#
# def writeTxt(path,mode) :
#     file = open(path, mode="w" , encoding="utf-8")
#     file.write("hi.welcome my home")
#
# # caller
# writeTxt('./data/test.txt', "w")

def with_open_file(path, mode , e ) :
    with open(path, mode, encoding=e) as file :
    # print(file.read()) # 전체 다 읽어옴
    # print(file.readline()) # 1줄
    # print(file.readlines())# 여러줄 리스트
    # line = file.readline
    # while line != '' :
    # print(line.strip('\n'))
        lst = file.readlines()
        for s in lst :
         print(s.strip("\n"))

with_open_file('data/greeting.txt', "r", "utf8")

# read 문자열
# readlies 리스트

