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



a = ['cde' , 'cfc' , 'abc']
def fn(s) :
    return s[0], s[-1]
print(sorted(a, key=fn))

# 그룹 애너그램

input = ['eat'  , 'tea' , 'tan' , 'ate' , 'nat' , 'bat']

s = sorted(input)
print(s)


def groupAnagrams(self,strs) :
    anagrams = collections.defaultdict(list)

    for word in strs :
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())


# 가장 긴 팰린드롬 부분 문자열

def longestPalindrome(self, s ) :
    def expand(left : int , right : int) :
        while left >= 0 and right < lens(s) and s[left] == s[rigth]
            left -= 1
            right += 1
        return s[left + 1:right]

    if lens(s) < or s == s[::-1] :
        return s

    result = ''

    for i in range(len(s) - 1 ) :
        result = max(result, expand(i, i +1), expand(i, i + 2), key = len )
        return result


