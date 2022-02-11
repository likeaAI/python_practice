'''
opp(객체지향 프로그래밍)
- class(변수 + 함수) - instance 생성할 수 있다.
-- 클래스에 정의된 구성요소 변수와 함수는 클래스의 소유가 아닌 인스턴스 소유다.
- initializer(초기화 함수, 생성자)
--magic function
- object vs instance
- 함수 < 클랙스 < 모듈(클래스(변수+함수)) < 패키지
- 명사적, 동사적 특징
- self <- 인스턴스를 대표하는 키워드
'''

# 강사의 정보를 저장할려고 한다.....

cls_var =  4.5

class Teacher :
    # 변수 + 함수
    cls_var = 3.5

    def doing(self):
        print('인스턴스 소유의 함수 입니다. ')

# class 안에 있는 doing이라는 함수를 호출하기 위해서는
#1. 클래스로부터 인스턴스 생성이 필요하다.
#2. 호출 instance.함수()


tea = Teacher() #인스턴스를 생성하는 코드 , 메모리상에 인스턴스 생성됨
tea.doing()

print('instance address -' , tea)
# 16진수 주소할당
print('instance function ', end='')
tea.doing()

# class Person :  opp파일에 생성해둠
#     # 이니셜라이즈
#     # 객체 생성시 자동생성
#
#     def __init__(self, name, subject, email): # 초기화 함수 initializer(magic function)
#         self.name    = name # self. 함으로써 인스턴스 소유가 된다!
#         self.subject = subject
#         self.email   = email
#
#     def perInfo(self):
#         return '이름 {}, 과목 {} , 메일 {} '.format(self.name, self.subject, self.email)



#
#
# per1 = Person('변윤섭', 'python' , 'crid2450@gmail.com')
# per2 = Person('변섭', 'ython' , 'crid0@gmail.com')
# per3 = Person('섭', 'ythn' , 'id0@gmail.com')
#
# lst = list()
# lst.append(per1)
# lst.append(per2)
# lst.append(per3)
#
# for instance in lst :
#     print(instance.perInfo())
#
#
# print(cls_var)
# print(Person.cls_var)
# print()
#

#
# class Employee : #  1. class 선언 클래명 작성
#     def __init__(self, userName, userSalary): #2 . 이니셜라이즈 초기화 함수 선언 및 인수 선언
#         print('초기화 함수 자동 호출')
#         self.userName = userName
#         self.userSalary = userSalary # 형태는 외울것. self가 없이는 제대로 작동하지 않음


from study.util.oop import * # opp.py 작성후 거기에 클래스 정의 해놈
#클래스 사용 예시
emp0bj01 =  Employee("나비" , 1000)
emp0bj02 =  Employee("단추" , 2000)
emp0bj03 =  Employee("호랑이" , 5000)
print(emp0bj01.getSalary())
print(emp0bj02.getSalary())
print(emp0bj03.getSalary())
emp0bj01.incrementSalary()
emp0bj02.incrementSalary()
emp0bj03.incrementSalary()
print('급여인인상 - ')
print(emp0bj01.getSalary())
print(emp0bj02.getSalary())
print(emp0bj03.getSalary())
Employee.raise_rate = 1.8 # 함수클래스를 변수값을 클래스명.함수 로 다시 재선언
emp0bj01.incrementSalary()
emp0bj02.incrementSalary()
emp0bj03.incrementSalary()
print('급여인인상 - ')
print(emp0bj01.getSalary())
print(emp0bj02.getSalary())
print(emp0bj03.getSalary())\

'''[실습]
1. Account class 작성 
2.  인스턴스 변수 - account, balance, interestRate'
3. accountInfo() - 계좌정보 출력하는 역활 
4. deposit(amount) - 매개변수들어온 amount 를 balance 입금한다. 
5. withDraw(amount) - 매개변수들어온 amount 를 balance 차감한다.
5-1 단) 잔고가 부족할 경우 '잔액이 부족합니다.'
6. printInterestRate() - 현재 잔액에 이자율을 계산하여 소수점  '''

# caller
# account1 = Account('441-2919-1234' , 500000 , 0.073)
class Account :
    def __init__(self, account , balance  , interestRate ) :
        self.account = account
        self.balance = balance
        self.interestRate = interestRate

    def accountInfo(self):
        print('계자번호{}, 잔액{} 출력-'.format(self.account, self.balance, self.interestRate))

    def withDraw(self, amount):  # 출금 할때는 if로 잔액을 비교하는 문구가 필요하다.
        if self.balance >= amount :
            self.balance -= amount # 이런 -+ += 이런 문법에 익숙해져라
            print("{}원만큼 출금하였습니다. 확인해주세요 ".format(amount))

        else :
            print('잔고가 부족합니다. ')

    def deposit(self,amount):
        self.balance += amount  # 이런 -+ += 이런 문법에 익숙해져라
        print("{}원만큼 입금하였습니다. 계좌잔액 {}원 입니다. 확인해주세요 ".format(amount, self.balance))
    def printInteretRate(self):
        self.balance = self.balance * (1 + self.interestRate)
        print('%.2f')

account1 = Account('441-2919-1234' , 500000 , 0.073)
account1.withDraw(500000)
account1.deposit(500000)
account1.deposit(100000000)
account1.accountInfo()
account1.printInteretRate()

'''
[실습2] 
'''


# car = Car("avante , 4, 1600 , 2400 )
#
# class Car :
#     def __init__(self, name , door, cc , price ):
#         self.utype = self.__class__.__name__ # class 정보 확인하는 명령어
#         self.name = name
#         self.door = door
#         self.cc = cc
#         self.price = price
#     def carinfo(self):
#         if self.cc >= 5000 :
#             self.grade('대형차')
#         elif self.cc >= 3000 :
#             self.grade('중형차')
#         else:
#             print("소형차 , 준소형차 ")
#         self.display()
#
#     def display(self):
#         print('자동차 모델은 {}이며  grade는 {} 가지고 있으며 \n{} 용량은,{}만원입니다.'.format(self.name,self.grade, self.cc , self.cc , self.price))
#
# car = Car('avante' , 4, 1600 , 2400 )
# print('사용하는 클래스는 -' , car.utype)
# car.display()


# oop (은닉화, 상속, 다형성, 추상화)
#(Object Oriented Programming)
#상속(Interitance) , object ( 최상위 클래스)
#부모 - 자식 관계 (is a ~ )
# A(A~Y) 상속을 하게 되면 기존 A에서 +(Z)만 추가 하여 사용 가능 A~Z모두 사용

# 상속은 기준으로 부모님돈도 자식꺼 내꺼도 내꺼 이런 개념으로 이해해라... -_

class unit(object): # 상속이란 .. 관계가 위로 올라갈수록 추상화가 된다. ???
    pass

class Marine(unit) : # unit을 상속받기 위해서 class unit을 마린이라는 클래스에 상속한다.
    pass

class Medic(unit) : # unit을 상속받기 위해서 class unit을 마린이라는 클래스에 상속한다.
    pass

# 은닉화(encapsulation) - information hidding ,
class userdata(object) : # 파이썬 상속 안하면 최상위 오브젝트를 상속받는다. 안해도 마찬가지
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

mydate = userdata(-2022, 13,50)
print('year -' , mydate.year)
print('month -' , mydate.month)
print('day -' , mydate.day)
#  이데이터 유효성 체크를 걸러내야  가능 , 외부에서 접근하지 못하게 한다.
#  직접적 변수 접근은 불가하지만 함수를 통한 간접은 허용한다. 뭔소리냐
# --> set. get. 간접허용 함수 예시
# class 답게 하려면 은닉 다향성 상속의 개념이 포함되어야 진정한 opp 이다.
