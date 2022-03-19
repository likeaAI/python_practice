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




# pig lattin
# a,e,i,o,u 끝나면 way 추가 , 그외에 첫글자 뒤로가서 ay 추가

word = "apple"
piglist = ["a","e","o","u","i"]
if word[0] in piglist :
    print("possible")

else :
    print("impossible")

# 다른 바식


pl_sentence ="this is a test translation"
def piglattin(pl_sentence):
    def01 = pl_sentence.split()
    new_sentence = []
    print(def01)
    for i in def01 :
        if i[0] in 'aeiou' :
            pig01 = i + "way"
            new_sentence.append(pig01)
        else :
            pig02 = i[-1]+ i + "ay"
            new_sentence.append(pig02)
    return ' '.join(new_sentence)

print(piglattin(pl_sentence))


def pl_sentence(sentence):
    output = []
    for word in sentence.split():
        if word[0] in 'aeiou':
            output.append(f"{word}way")
        else:
            output.append(f"{word[1:]}{word[0]}ay")

    return ' '.join(output)

print(pl_sentence('this is a test'))






