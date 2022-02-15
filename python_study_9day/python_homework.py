'''
# 1. displ(배기량)이 4 이하인 자동차와 6 이상인 자동차 중
# 어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 확인하세요.

# 2. 자동차 제조 회사에 따라 도시 연비가 다른지 알아보려고 한다.
# "audi"와 "toyota" 중 어느 manufacturer(제조회사)의 cty(도시 연비)가
# 평균적으로 더 높은지 확인하세요.

# 3. "chevrolet", "ford", "honda" 자동차의 고속도로 연비 평균을 알아보려고 한다.
# 이 회사들의 데이터를 추출한 후 hwy(고속도로 연비) 평균을 구하세요.

# 4. "audi"에서 생산한 자동차 중에 어떤 자동차 모델의 hwy(고속도로 연비)가
# 높은지 알아보려고 한다. "audi"에서 생산한 자동차 중 hwy가 1~5위에 해당하는
# 자동차의 데이터를 출력하세요.

# 5. mpg 데이터는 연비를 나타내는 변수가 2개입니다.
# 두 변수를 각각 활용하는 대신 하나의 통합 연비 변수를 만들어 사용하려 합니다.
# 평균 연비 변수는 두 연비(고속도로와 도시)의 평균을 이용합니다.
# 회사별로 "suv" 자동차의 평균 연비를 구한후 내림차순으로 정렬한 후 1~5위까지 데이터를 출력하세요.

# 6. mpg 데이터의 class는 "suv", "compact" 등 자동차의 특징에 따라
# 일곱 종류로 분류한 변수입니다. 어떤 차종의 도시 연비가 높은지 비교하려 합니다.
# class별 cty 평균을 구하고 cty 평균이 높은 순으로 정렬해 출력하세요.

# 7. 어떤 회사 자동차의 hwy(고속도로 연비)가 가장 높은지 알아보려 합니다.
# hwy(고속도로 연비) 평균이 가장 높은 회사 세 곳을 출력하세요.

# 8. 어떤 회사에서 "compact" 차종을 가장 많이 생산하는지 알아보려고 합니다.
# 각 회사별 "compact" 차종 수를 내림차순으로 정렬해 출력하세요.

csv 리드 쓰지말고 순수 파이썬 형식으로 해결하시오! , class로 풀기 권함, 왜냐면 그게 쉬움 ,
hint - mgp.py
평균사용법
import mpg as m (클래스로 가져와라 )
from  statistics import mean ()
'''
# 데이터를 가져오기
# mpgLst = []
# with open('data/mpg.txt', 'r' , encoding='utf-8') as file :
#     file.readline()
#     line = file.readline()
#     while line != '' :
#         row = line.strip('\n').split(',') # 텍스트파일을 정리
#         mpgLst.append(row)
#         line = file.readline()

# class를 사용할 생각이라면..
#     while line != '' :
#         row = line.strip('\n').split(',') # 텍스트파일을 정리
#         # mpgLst.append(row)
#         instance = m.Mpg(row[0],row[1], ................row[10])
#         line = file.readline()

# print(mpgLst) # mpgLst[0][0]
# print(mpgLst[0][0]) # audi

# 본인이 여기서부터 코딩 , # 먼저 csv 파일을 불러올것.
#
# with open('./data/mpg.txt' , 'r' , encoding ='utf-8') as file :
#     data = file.readlines()
#     for redata in data :
#         print(redata)
from  statistics import mean
mpgLst = []
with open('data/mpg.txt', 'r' , encoding='utf-8') as file :
    file.readline() # header 를 건너뛴다..
    line = file.readline()
    while line != '' :
        row = line.strip('\n').split(',') # 텍스트파일을 정리
        mpgLst.append(row)
        line = file.readline()
# print(mpgLst)
# print(mpgLst[0][4])
# print(type(int(mpgLst[0][4]))) # int형으로 추출하는것이 가능하다.
# with open('data/mpg.txt', 'r' , encoding='utf-8') as myfile:
#     total_lines = sum(1 for line in myfile)
# print(type(total_lines)) 235
# while 구문은 생각이 안나서 for 구문 텍스트 안에 전체 행수를 구하고 그걸 그냥
# for문에 때려박았다 ;
hwl4 = []
hwl6 = []
for i in range(0 , 234) : # 이걸 프로그램상으로 어떻게 구현해야할까...
    hwl = [mpgLst[i][1], mpgLst[i][4] , mpgLst[i][8]]
    for j in range(0,234) :
        if int(mpgLst[j][4]) <= 4 :
            hwl4.append(mpgLst[j][1], mpgLst[j][4] , mpgLst[j][8])
        elif int(mpgLst[j][4]) >= 6 :
            hwl6.append(mpgLst[j][1], mpgLst[j][4] , mpgLst[j][8])
    # 배기량을 기준으로 4와 6을 리스트로 분리 완료
print(hwl4)



    # print(hwl) # 모든 리스트에서 배기량 의 값을 뽑아냈다. 그렇다면 연비도 같이 표현할수있을까 , 딕셔너리로 같이 묶었다.
    # hwl 딕셔너리의 키값은 배기량이고 벨류는 연비를 의미한다. 이걸 사용할수 있을까 ?


