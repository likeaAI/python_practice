import random as r

print("leve1 확률 10% 도전할 기회를 10번정도로 추천합니다." )
print("leve2 확률 1% 도전할 기회를 100번정도로 추천합니다.")
print("leve3 확률 0.1% 도전할 기회를 1000번정도로 추천합니다.")
start = int(input("업그레이드 시작 ! level을 선택하세요 : "))
w_life = int(input("도전할 기회를 정하세요 : "))
try_life = 0
for _ in range(w_life) :


    if start == 1 :
        print("레벨 1 무기를 업그레이드 합니다. 확률은 10% 이며 재도전 기회는 {}번입니다.".format(w_life))
        w_percentage = 1
        user_percentage = r.randint(1, 11)
        if w_percentage == user_percentage :
           print("성공했습니다. {}만에 성공했습니다.".format(try_life))
           start += 1

        else :
            w_life -= 1
            try_life += 1
            print(" 실패했습니다. 도전기회는 {}회 입니다.".format(w_life))

    elif start == 2 :
          print("레벨 2 무기를 업그레이드 합니다. 확률은 1% 이며 재도전 기회는 {}번입니다.".format(try_life))
          w_percentage = 1
          user_percentage = r.randint(1, 101)
          if w_percentage == user_percentage :
             print("성공했습니다. {}만에 성공하였습니다. ") # 횟수를 어떻게 표현해야 할가 97번이면
             start += 1

          else:
             w_life -= 1
             try_life += 1
             print(" 실패했습니다. 도전기회는 {}회 입니다.".format(w_life))


    elif start == 3 :
          print("레벨 2 무기를 업그레이드 합니다. 확률은 0.1% 이며 재도전 기회는 {}번입니다.".format(w_life))
          w_percentage = 1
          user_percentage = r.randint(1, 1001)
          if w_percentage == user_percentage :
             print("성공했습니다. 축하합니다. 레벨 3모두 통과하였습니다. 복권이나 확률형 현질 아이템을 해보시길 바랍니다.")


          else:
             w_life -= 1
             try_life += 1
             print(" 실패했습니다. 도전기회는 {}회 입니다.".format(w_life))




