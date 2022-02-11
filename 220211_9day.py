# 파일입출력
# xxx.csv 파일 , xxx.xls
# 분석 - ndarray(list와는 다르다 list와는!), dataFrame , Series
# AJAX - 비동기 통신 (Restful Service)
# json - {key : {key : value } , key : [{key : value}] , {key : value}] }

#회문(palindrome) ? : tomato , madam, sos, level, rotator, nurses run
# 회문을 검사하는 함수를 만들어 본다면 ?

# word = "sos"
# if word == word[::-1] :
#     pass
#
# if list(word) == list(reversed(word))
 #pass

# for i in ragne(len(word)
    # if word[i] != word[-1-i]

# palindrome_words.txt 파일로부터 회문인 단어만 출력하고
# 카운팅 해 본다면
# 주의) 단어의사이의 줄바꿈이 2번 일어나면 안된다.

# ex1) 실패...
# with open("./data/palindrome_words.txt", "r" , encoding="utf-8") as file2 :
#     for line in file2 :


# ex2) 어렵게? 다양하게?
# def que04():
#     with open("./data/palindrome_words.txt", "r" , encoding="utf-8") as file :
#         cnt = 0
#         for line in file :
#             # print(type(line), line )
#             isFlag =True
#             line = line.strip("\n")
#             for i in range(len(line)//2) : # 2로나우서 단어 가운데 중심을 맞춘다.
#                 if line[i] != line[-1-i] :
#                     isFlag = False
#                     break
#                 if isFlag :
#                     cnt += 1
#                     print(line)
#     print('회문 단어의 갯수는 : {} 입니다. .'.format(cnt))
#     # 왜 안되지 ; ?

import pandas as pd
# pd.read_csv() - DataFrame  : csv 읽는 모듈
# pd.ExcelFile() - DataFrame  : 엑셀 읽는 모듈
def load_file(filePath) :
    data = None
    if filePath.split('.')[-1] == 'csv' :
        data = pd.read_csv(filePath, encoding="ms949" ) # header =None 헤더를 데이터로 반환해버린다.
    elif filePath.split('.')[-1] == 'xls' :
        pass
    else :
         pass
    return data
# label 컬럼을 활용하여 빈도수를 출력하는 구문을 작성해본다면 ?
# dict 형식으로
# 내가 생각한 정리
# 1. 라벨을 분리 , 2. 라벨 갯수를 체크 3. 딕트타입으로 재정의 ex ) 변수 =  { label1 : 빈도수 , .........}

def csv_file(filepath) :
    data = load_file(filepath)
    # print('type -' , type(data))
    # print(data.head())
    # print(data.info())
    # print(type(data.height))
    # print(data['height'])
    # print(data.label)
    lblFreq = {}
    for key in data.label :
        lblFreq[key] = lblFreq.get(key, 0) + 1

    print(lblFreq)



# caller

csv_file('./data/service_bmi.csv')

