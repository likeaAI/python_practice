# '''
# 1. input 함수를 이용해서 연도와 월을 입력
# 2. 해당년도가 윤년일 경우 2월달의 마지막일은 29, 평년일 경우 2월당의 마지막일은 28
# 출력형식  : xxxx년 x월 마지막일은 xx일 입니다.
# '''
#
# '''
# 윤년의 조건
# '''
# # year = 2024
# # if (year%4 == 0  and year%100 != 0) or year%400 == 0  :   # != 아니거나 not equal
# #     print('leap year')
# # else :
# #     print('year')
# #
# dict_cal1 = {1 : '31일' ,  2 : '29일' , 3 : '31일' , 4 : '30일' , 5 : '31일' , 6 : '30일'
#              , 7: '31일' , 8 : '30일' , 9 : '30일' , 10 : '31일' , 11 :'30일' , 12 :'31일'}
#
# dict_cal2 = {1 : '31일' ,  2 : '28일' , 3 : '31일' , 4 : '30일' , 5 : '31일' , 6 : '30일'
#              , 7: '31일' , 8 : '30일' , 9 : '30일' , 10 : '31일' , 11 :'30일' , 12 :'31일'}
#
# year_input = int(input('년도를 입력하세요 : '))
# month_input = int(input('월을 입력하세요  : '))
#
# if (year_input%4 == 0  and year_input%100 != 0) or year_input%400 == 0 :
#     print('{}년 {}월 마지막일은 {} 입니다.'.format(year_input,month_input,dict_cal1.get(month_input)))
#
# else :
#     print('{}년 {}월 마지막일은 {} 입니다.'.format(year_input,month_input,dict_cal2.get(month_input)))
#
# # list로 표현해서 -1을 사용하는 방법
#
#
# # 시간이 입력될때 입려된 시간이 정각인지 아닌지를 구분하고 싶다면
# # 시,분 h,m 비교  14:12 -> true , false 구분
# #
# # time = '14:56'
# # print(time[3:])
# # if time[3:] == '00' :
# #     print("정각입니다.")
# # else :
# #     print("정각이 아닙니다.")
# #
# # # 3항 연산자를 활용하는 법
# # result = '정각' if time[-2:] == '00' else '정각이 아닙니다.'
# # print(result)
# # # split을 활용하는법
# # result2 = '정각' time.split(':')[1] == '00'  else '정각이 아닙니다.'
# # print(result2)
# #
#
# #011  = sk  016=ktf , 019 lguplus
# # 011-1234-1234 통신사 번호를 식별하고 싶다.
#
# phone_number = '011-1234-1234'
# if phone_number[:3] == '011' :
#     print('sk통신사입니다.')
# elif phone_number[:3] == '016' :
#     print('ktf통신사입니다.')
# elif phone_number[:3] == '019' :
#     print('lgu통신사입니다.')
#
# # 0~8 서울 나머지는 지방
# # 주민번호 881011-1073913 성별과 출생지역을 출력하라.
#
# slavenum = '881011-1073913'
# gender = slavenum.split('-')[1]
#
# # 가장핵심은 00~08 까지를 간결히 표현할것인가. 08까지가 서울 나머지는 지방 ,
# # 나머지는 간단히 표현가능 00~08까지 경우의 수를 어떻게  ?
#
#
# result = '남자' if gender[0]=='1' or gender[0] == 3 else '여자'
# location = 'seuoul' if int(gender[1:3] in range(0,9)) else 'not seoul'
# # int(gender[1:3] in range(0,9)) <- 00~08까지 표현방법
# print(result , location)


# while 예제 10번으로 숫자를 맞춰라.
from random import randint
answer = randint
answer = randint(1,100)
print('answer -' , answer)


tries = 1
while tries <= 10 :
    input_number = int(input("숫자를 입력하세요 :  "))
    if answer == input_number :
        print("정답{} 정답입니다.".format(answer))
        break
    elif answer > input_number :
        print("입력하신 숫자보다 정답은 큽니다. 다시 입력해보세요 ")

    elif answer < input_number :
        print("입력하신 숫자가 정답은 작습니다. 다시 입력해보세요 ")

    tries += 1

print("정답 {} , 시도횟수 {}".format(answer , tries ))









