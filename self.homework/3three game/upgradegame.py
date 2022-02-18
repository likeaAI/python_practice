import random as r

start = int(input("업그레이드 시작 ! level을 선택하세요 : "))
w_life = int(input("도전할 기회를 정하세요 : "))
print("leve1")
print("leve2")
print("leve3")

if start == 1 :
    print("레벨 1 무기를 업그레이드 합니다. 확률은 10% 이며 재도전 기회는 {}번입니다.".format(w_life))
    w_percentage = 1
    user_percentage = r.randint(1, 11)
    for _ in range(w_life) :
        if w_percentage == user_percentage :
           print("성공했습니다.")
           start == 2

        else :
            w_life -= 1
            print(" 실패했습니다. 도전기회는 {}회 입니다.".format(w_life))




