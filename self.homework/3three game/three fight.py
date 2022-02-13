# 가위바위보 3판 2선제를 구현해보자.
# 사용자가 메인에서 1,2,3, 가위 바위 보를 고를 수 있게하자.

import random as rd
gamedict = {1:"가위" , 2:"바위" , 3:"보"}

# 메인화면

print("컴퓨터와 가위바위보 게임 3판 2선승제 ")
print( " 1. 가위 ")
print( " 2. 바위 ")
print( " 3. 보 ")


# 승점포인트 선언

user1 = 0
cpu = 0
match = 0
# 컴퓨터와 가위바위보 게임 구현
# 모두 비기는 경우의 수
for i in range(10) :
    user = input("가위,바위, 보 중에 낼것을 입력해주세요 : ")  # 나중에 가위바위보만 입력하게 할수있을까  ?
    com = 1
    comvs = gamedict.get(com)

    if user1 == 3 :
        print("사용자가 {}판으로 이겼습니다.".format(user1))
        print("사용자가 {}점 ,컴퓨터가{}점 ".format(user1, cpu))
        break
    elif cpu == 3 :
        print("컴퓨터가 {}판으로 이겼습니다.")
        print("사용자가 {}점 , 컴퓨터가{}점 ".format(user1, cpu))
        break


    # user 가위를 냈을때
    elif user == "가위" and comvs == "바위" :
        cpu += 1
        print("{} vs {} 컴퓨터가 이겼습니다.".format(user,comvs))

    elif user == "가위"  and comvs == "보" :
        user1 += 1
        print("{} vs {} 사용자가 이겼습니다.".format(user,comvs))

    # user 가 바위를 냈을때

    elif user == gamedict.get(2) and comvs == "보" :
        cpu += 1
        print("{} vs {} 컴퓨터가 이겼습니다.".format(user,comvs))

    elif user == gamedict.get(1) and comvs == "가위" :
        user1 += 1
        print("{} vs {} 사용자가 이겼습니다.".format(user,comvs))

    # user 가 보를 냈을때
    elif user == gamedict.get(3) and comvs == "가위" :
        cpu += 1
        print("{} vs {} 컴퓨터가 이겼습니다.".format(user,comvs))

    elif user == gamedict.get(3) and comvs == "보" :
        user1 += 1
        print("{} vs {} 사용자가 이겼습니다.".format(user,comvs))

    elif user == comvs :
         print("{} vs {} 비겼습니다.".format(user,comvs))

    match += 1