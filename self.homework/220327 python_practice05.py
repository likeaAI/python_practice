# 로그 파일 재정렬
import collections

logs = ['dig1 8 1 5 1 ' , 'let1 art can', 'dig2 3 6' , ' let2 own kit dig' , 'let3 art zero']

# 람다와 + 연산자 이용

# digits =[]
# letters = []
# if log.split()[1].isdigit() :
#     digits.append(log)
# else :
#     letters.append(log)

def reorderLogFiles(self) :
    letters, digits = [],[]
    for log in logs :
        if log.split()[1].isdigit():
            digits.append(log)
        else :
            letters.append(log)

    letters.sort(key=lambda x : (x.split()[1:] , x.split()[0]))
    return letters + digits


print(reorderLogFiles(logs))


# 가장 흔한단어

paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit.'
banned = ['hit']

# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라
# 대소문자 구분을 하지 않으며 구두점 또한 무시한다.

'''
1. split으로 paragrahp를 자른다. 그리고 카운터로 각 단어별 중복횟수를 나타낸다. 
2. 금지된 단어 처리 

'''
from collections import Counter
import re

def mostCommonWord(self, paragraph) :
words = [word for word in re.sub(r'[^\w]', ' ' , paragraph)  \
    .lower().split()\
    if word  not in banned ]

counts = collections.Counter(words)
return counts.most_common(1)[0][0]