'''[실습]
1. Account class 작성
2.  인스턴스 변수 - type(S|F) ,  account, balance, interestRate'
2-1 SavingAccount , FundAccount - Account 상속받는....
3. accountInfo() - 계좌정보 출력하는 역활
4. deposit(amount) - 매개변수들어온 amount 를 balance 입금한다.
5. withDraw(amount) - 매개변수들어온 amount 를 balance 차감한다.
5-1 단) 잔고가 부족할 경우 '잔액이 부족합니다.'
6.abstract printInterestRate() - 현재 잔액에 이자율을 계산하여 소수점 # 추상클래스
- 2-1 SavingAccount , FundAccount - Account 상속받는.... -- printInterestRate() 함수를 오버라이딩
SavingAccount - printInterestRate() 기본 이자율에 만기시 이율이 0.1
FundAccount - - printInterestRate() 기본 이자율에 잔액이 10만원이상이면 10%
            기본 아지율이 잔액이 10만원이상여면 10%
            기본 이자율에 잔액이 50만원이상이면 15%
            기본 이자율에 잔액이 100만원이상이면 20%
'''

from abc import *

class Account :
    def __init__(self, account , balance  , interestRate , ) :
        self.account = account
        self.balance = balance
        self.interestRate = interestRate

    def accountInfo(self):
        print('계좌번호{}, 잔액{} ,출력-'.format(self.account, self.balance, self.interestRate, ))

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
        return self.balance
        print("만기시 예상금액은 ", self.balance ,"원이며" ,"만기시 예상 이자는 {} 입니다.".format(1+self.interestRate))

class abstract_printInterestRate(metaclass=ABCMeta) :
    @abstract_printInterestRate
    def abstractmethod(self) :
        pass

class SavingAccount(Account):
    def __init__(self, account, balance, intersRate , typeS):
        super().__init__(account, balance, intersRate)
        self.typeS = typeS

    def printInteretRate(self):
        self.balance = self.balance * 1.01
        print("만기시 예상금액은 ", self.balance, "원이며", "만기시 예상 이자는 0.1% 입니다.")



class FundAccount(Account) :
    def __init__(self, account, balance, intersRate , typeF):
        super().__init__(account, balance, intersRate)
        self.typeF = typeF

    def printInteretRate(self):
        if  100000 <= self.balance < 500000 :
            self.balance = self.balance * 1.1
        elif 5000000 <= self.balance < 1000000 :
            self.balance = self.balance * 1.15
        elif  self.balance >= 1000000  :
             self.balance = self.balance * 1.20
        else :
            self.balance = self.balance * 1.01

        print("만기시 예상금액은 ", self.balance, "원이이다.")



test2 = SavingAccount('111-111-111111' , 465000, 0.4 , 'Stype')
print(test2.accountInfo())
print(test2.printInteretRate())

test3 = FundAccount('002-004-5123' , 1000000 , 0.55555, 'Ftype')
print(test3.accountInfo())
print(test3.printInteretRate())
