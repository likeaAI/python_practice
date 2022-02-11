
#------ [실습] -----
movie_list = ['이터널스', '스파이더맨' , '매트릭스', '경관의 피', '샹치' , '스타워즈' , '아이언맨']
# type check
print('type - ', type(movie_list))
  # ->  결과  class list
print('data -' , movie_list)
 # indexing 추측 ['이터널스', '스파이더맨', '경관의 피 ', '샹치', '스타워즈', '아이언맨']

'''요구사항 
1번 모가디슈를 추가  <- append , extend 사용
2번 스파이더맨과 매트릭스 사이에 임섭순을 추가 <- 
3번 경관의 피를 삭제 
4번 . 매트릭스와 샹치를 삭제
5번 이터널스의 인덱스를 구해서 pop()함수를 이용한 삭제 
6번 최종리스트를 출력  
'''

#1
movie_list.append("모가디슈")
print(movie_list) # clear

#2
movie_list.insert(2, "임섭순" )
print(movie_list)

#3
movie_list.remove("경관의 피")
print(movie_list)

#4
del movie_list[3]
del movie_list[3]
print(movie_list)

#5
idx = movie_list.index("이터널스") #0을 반환
movie_list.pop(idx)
print(movie_list)


#6
#['스파이더맨', '임섭순', '스타워즈', '아이언맨', '모가디슈']



#1~99 까지의 정수 중 짝수만 튜플에 저장한다면 ?
# 1. 짝수를 구현하는 법 range(2,100,2)

even_data = tuple(range(2,100,2))
print('type - ' , type(even_data), even_data)






