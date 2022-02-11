
# while 구문을 이용한 10고개 숫자 퀴즈
from random import randint
answer = randint(1, 100)
print('answer - ' , answer)
tries = 1
while tries <= 10 :
    guess  = int(input('1 ~ 100 사이의 값을 입력하세요 : '))
    if   answer == guess :
        break
    elif guess > answer :
        print('down')
    else :
        print('up')
    tries += 1

print('정답 {} , 시도횟수 {}'.format(answer, tries))
