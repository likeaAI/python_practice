

# dict 실습
# 단어의 빈도수를 구하기 {'love' : 2 , 'word : 2' , 'cat : 1 '}
# get 함수의 인자 ( ' ' , 'default')
word_vec = ['love' , 'word' , 'love' , 'cat' ,  'word']
print('len - ' , len(word_vec))  # len 반환값은 5


# 1.***** 어렵다 잘 이해가 안가네
# for loop 예제라든지 활용이라든지 보강필요

wc = {} # 1 딕트형을 만든다.
for word in word_vec : # for loop문으로 word_vec 만큼 돌린다. word변수 이름은 아무래도 상관없음
    wc[word] = wc.get(word, 0) + 1 # wc[word] -> wc[1] , wc[2]
print('wc - ', wc)


#5 set, zip

# set으로 중복값을 날리는 것 가능  , 카운터로 리스트 갯수 표기 , zip으로 나중에 합치기
# 컴프리핸션 테크닉 익혀두자 !

print(set(word_vec))
print([word_vec.count(i) for i in set(word_vec)])

result = dict(zip(set(word_vec),[word_vec.count(i) for i in set(word_vec)]))
print(result)
