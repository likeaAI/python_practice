
#1 Que 1
#1) special_words.txt 파일로부터 문자 'c' 포함된 단어를 출력
#2)  단어를 출력할때 등장한 순서대로 출력

with open("special_words.txt" , "r" , encoding="utf-8") as f :
    lines = f.readline().split()
    lines = [i.strip(',.') for i in lines]
    print(lines)
    for word in lines :
        if 'c' in word :
            print(word)

# 초반에 핵심 키워드는 맞춤 구현을 못함
# if in의 사용법은 여전히 못하고
# list 컴프리핸션으로 자잘한 기호 날리기는 못함

# 핵심인 단어분리와 정규식 이용이라는 입출력은 어쨋든 접근함

#que 2
# special_words.txt 파일로부터 단어의 길이가 10이하의 단어를 출력하고 카운팅하세요

with open("special_words.txt" , "r" , encoding="utf-8") as f :
    cnt = 0
    lines = f.readline().split()
    lines = [i.strip(',.') for i in lines]
    print(lines)
    for word in lines :
        if 10 >= len(word) :
            cnt += 1
            print(word)
    print("10글자 이하 단어수는 : {} 개".format(cnt))


#3 zipcod.txt
# input()함수를 이용해서 동 이름을 입력받아
# 예)개포
# 해당하는 동의 주소를 출력하는 함수를 정의한다.
# hint : \t
# startswith() 함수
# 예외처리

#! 각 행을 포구문형식으로 한줄씩 읽으면서 데이터가 조건이 맞으면(input) if문을 이용해서 함수로 구분후 반환한다.
def que03():
    pass

with open("zipcode.txt" ,"r" , encoding="utf-8") as disk :
    dong = str(input("동을 입력하세요 : "))
    originjuso = disk.readline()
    count = 0
    while True :
        juso = originjuso.split()
        juso = [i.strip(',.') for i in juso]
        if dong in juso :
            count += 1
            print(originjuso)
        elif :
            if originjuso == False :
                break

            print("검색 동수 : ", count, "개")


 # for word in lines :
 #        if 'c' in word :
 #            print(word)


