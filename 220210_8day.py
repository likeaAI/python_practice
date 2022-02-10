'''
학습목표
- 예외처리
- 매직함수, 데코레이터, 제너레이터 , 일급함수
- 파일 입출력
'''


# 예외처리 - ex) int형만 입력하는 란에 str입력해서 에러가 난다면 ...
'''
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
    
 '''

# function define - worker
def smpInput() :
    try :  # 단독 실행이 불가 쌍을 이뤄야 함 Try :  ~ except a :
        age = int(input('나이를 숫자로 입력해 주세요  :  '))
        print('your age is ' , age, ' years old')
    except ValueError as e :
        print(str(e))

# caller
smpInput()
print("programing end - ")