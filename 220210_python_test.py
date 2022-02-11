
#1 Que 1
#1) special_words.txt 파일로부터 문자 'c' 포함된 단어를 출력
#2)  단어를 출력할때 등장한 순서대로 출력

# with open("special_words.txt" , "r" , encoding="utf-8") as f :
#     lines = f.readline().split()
#     lines = [i.strip(',.') for i in lines]
#     print(lines)
#     for word in lines :
#         if 'c' in word :
#             print(word)

# 초반에 핵심 키워드는 맞춤 구현을 못함
# if in의 사용법은 여전히 못하고
# list 컴프리핸션으로 자잘한 기호 날리기는 못함

# 핵심인 단어분리와 정규식 이용이라는 입출력은 어쨋든 접근함

#que 2
# special_words.txt 파일로부터 단어의 길이가 10이하의 단어를 출력하고 카운팅하세요

# with open("special_words.txt" , "r" , encoding="utf-8") as f :
#     cnt = 0
#     lines = f.readline().split()
#     lines = [i.strip(',.') for i in lines]
#     print(lines)
#     for word in lines :
#         if 10 >= len(word) :
#             cnt += 1
#             print(word)
#     print("10글자 이하 단어수는 : {} 개".format(cnt))


#3 zipcod.txt
# input()함수를 이용해서 동 이름을 입력받아
# 예)개포
# 해당하는 동의 주소를 출력하는 함수를 정의한다.
# hint : \t
# startswith() 함수
# 예외처리

#! 각 행을 포구문형식으로 한줄씩 읽으면서 데이터가 조건이 맞으면(input) if문을 이용해서 함수로 구분후 반환한다.
def que03():
    adress = str(input("주소를 입력해주세요 : "))
    try :
        with open("zipcode.txt" ,"r" , encoding="utf-8") as f :

            for i in range(0,65000) : # 좀더 멋있는 식이 있겠지만 일단 이걸로 ????
                line = f.readline()
                renew = line.split("\t")
                serch = renew[3].count(adress) # count랑 startwith 는 값을 왜 true랑 false로 반환하냐 ? 해깔리게
                                            # startswith 는 리스트라 못쓴다고 한다......
                if serch == True : # serch 값이 투르면 트루값 만 해당하는 line을값을 print해라
                    print(line)
    except Exception as e :
        print(str(e))


def que03_1() :
    dong = input('동 입력하세요 예) 개포 : ')
    try :
        with open("zipcode.txt", "r" , encoding="utf-8") as file :
            line2 = file.readline()
            while line2 : # line2 가 계속 True 걸리다가 마지막에 Flase걸리면서 종료...;
                addr_lst = line2.split("\t")
                if addr_lst[3].startswith(dong) :
                    print(addr_lst)
                line2 = file.readline()  # 작업이 끝나고 다시 읽어드리는 명령어

    except Exception as e :
            print(str(e))


que03()

























