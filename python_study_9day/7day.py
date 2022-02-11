# class 상속

class Super() :
    def __init__(self):
        pass
    def super_fucnction(self):
        print('부모의 소유함수')

    def sayEcho(self, name):
       return name + "님, 즐거운 코딩하렴 . "


class sub(Super) :
    def __init__(self):
        pass
    def sub_function(self):
        print('본인 소유함수 - sub_function')

    def sayEcho(self, name):
        return name+ "님, 즐거운 코딩하겠습니다."

# 인스턴스 생성 ?
# child = Super()
# child.sub_function()
# child.sub_function()

# parent = Super()
# parent.super_function()
# parent.sub_function()
# 부모객체는 자식에 대한 객체 접근이 불가하다. 반대로 자식은 부보객체에 대한 접근(상속)이 가능하다.
# 자식객체가 있다면 부모객체에 의미가 크게 없다. 어자피 자식으로 객체 생성을 하면 다 포함되기 때문에

# 함수 재지정 (overriding ) - 다향성


# self, super <- 상속관계에서 부모를 지칭하는 별칭
# class Unit(object) :
#     def __init__(self, damage, life):
#         self.utype = self.__class__.__name__ # 어떤 클래스로 생성된는지 타입 확인가능
#         self.damage = damage
#         self.life = life
#
#     def status(self):
#         return '타입 {}  , \t 공격력 :{} \t 생명력 : {} \t  '.format(self.utype, self.damage, self.life)
#
#
# class Marine(Unit) :
#     def __init__(self, damage, life , offenseup, defenseup):
#         self.utype = self.__class__.__name__
#         super().__init__(damage,life)   # 부모클래스이 __ininit__ 호출하는 함수이다.
#         self.offenseup = offenseup
#         self.deffenseup = defenseup
#
#    def attack(self) :
#         print("마린이 공격을 시작합니다. ")
#
#    def stimPack(self) :
#        if self.life > 40 :
#            print('stimpack 사용합니다.')
#        else :
#            print('체력이 낮아 stimpack 사용 불가 ')
#
#
# #1)** 부모클래스에서 자식 상속 클래스에 오버라이딩 기능으로 추가하거나 변경 (함수의 재지정)
#     def status(self):
#         return super().status() + '공격력업글 : {} \t 방어력 업글 : {}'.format(self.offenseup, self.deffenseup)
#
#
#  class Medic(Unit) :
#      def __init__(self, damage, life , defensueup):
#
#
# # unit = Unit(100 , 100)
# print('info - ' , unit.status())


# 오펜스와 디펜스를 할당했으나 status에 표현하는 함수 표현이 없다.
#  1)** 함수 다형화 오버라이등 기능으로 오펜스와 디펜스를 추가 하자
class Unit(object) :
    def __init__(self, damage, life):
        self.utype  = self.__class__.__name__
        self.__damage = damage
        self.__life   = life
    def status(self):
        return '타입 : {}\t공격력 : {}\t생명력 : {}\t'.format(self.utype, self.__damage, self.__life)
    def attack(self):
        pass
    #################### set, get
    def setDamage(self, damage):
        self.__damage = damage
    def setLife(self, life):
        self.__life = life
    def getDamage(self):
        return self.__damage
    def getLife(self):
        return self.__life

class Marine(Unit) :
    def __init__(self, damage, life, offenseUp, defenseUp):
        self.utype = self.__class__.__name__
        super().__init__(damage, life)
        self.offenseUp = offenseUp
        self.defenseUp = defenseUp

    def status(self):
        return super().status()+'공격력 업글 : {}\t방어력 업글 : {}'.format(self.offenseUp, self.defenseUp)
    def attack(self):
        print('마린이 공격을 시작합니다. 땅!!땅!!땅!!')
    def stimPack(self):
        if self.getLife() > 40 :
            print('stimPack 사용합니다.')
            super().setDamage( super().getDamage() * 1.5)
            super().setLife( super().getLife() - 10 )

        else :
            print('체력이 낮아 stimPack 사용 불가!!')


class Medic(Unit) :
    def __init__(self, damage, life, defenseUp):
        self.utype = self.__class__.__name__
        super().__init__(damage, life)
        self.defenseUp = defenseUp
    def status(self):
        return super().status() + ' 방어력 업글 : {}' .format(self.damage)

    def attack(self): # 오버라이딩 동일한 함수를 구현하지만 각각 다른내용을 표현하고 있다. 다향성
        print('메딕이 마린을 치료합니다. +++ ')



print('marine 과 medic을 수송하고 수송기 Unit 설계 ')
class DropShip(Unit) : # Unit 을 상속받는다는건 life와 damage를 같이 쓴다는 의미
    def __init__(self, damage, life ):
        self.utype = self.__class__.__name__
        super().__init__(damage, life)
        self.unitlst = []

    def board(self, crew):
        self.unitlst.append(crew)

    def drop(self):
        for u in self.unitlst :
            print('info - ' , u.status())
    def move(self):
        print('병력을 타겟지점으로 이동시킵니다. ')


print('DropShip 생성 - ', )
ship = DropShip(0, 100)
print(ship.status())
print('부대원 이동을 위해서 DropShip 승선시킨다. - ')

# 다중 상속
# 추상화
# from abc import * <- 추상함수 임포트 방법 : 추상 매소드 ; 함수에 구현부가 없음
from abc import *




class Tiger :
    pass

class Lion :
    pass
class Liger(Tiger, Lion)







# 추상화

