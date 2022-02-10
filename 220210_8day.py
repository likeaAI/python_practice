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
exceptionFunc(usrlsr)