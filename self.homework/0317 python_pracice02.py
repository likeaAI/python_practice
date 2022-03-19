# *numbers 역활

def mysum(*numbers) :
     output = 0
     for number in numbers :
         output += number
     return output

# 실행
print(mysum(10,20,30,40))


#
# time_list = []
# while True :
#     time = input('Enter 10Km run time : ')
#     time_list.append(time)
#
#     if time == '' :
#         s = divmod(time_list, len(time_list))
#         print(s)
#         break


def run_timing():
    """사용자에게 숫자 입력을 여러 개 받고, 그 평균을 출력합니다. """
    number_of_runs= 0
    total_time = 0

    while True :
        one_run = input('Enter 10 Km run time : ')

        if not one_run :
            break

        number_of_runs += 1
        total_time += float(one_run)


    average_time = total_time / number_of_runs
    print(f'Average of {average_time}, over {number_of_runs} runs')

run_timing()


