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
        if 5 >= len(word) :
            cnt += 1
            print(word)
    print("10글자 이하 단어수는 : {} 개".format(cnt))


#3 zipcod.txt
# input()함수를 이용해서


