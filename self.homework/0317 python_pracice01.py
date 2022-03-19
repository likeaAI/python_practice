import random as r


def game1() :
    com = r.randint(1,100)

    while True:
        user = int(input("니 생각은 어떤대 숫자는? "))
        if user == com :
            print(f'미쳤네 이걸맞춰? 컴퓨터는 {com} 숫자를 생각함')
            break
        elif user > com :
            print(f'너무 높게 불렀네 좀 낮춰봐 {user}')

        else :
            print(f'너무 낮게 불렀네 좀 높여봐 {user}')

game1()

