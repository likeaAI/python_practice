
text = '''
This is a test file.

It contains 28 words and 20 different words.

It also contains 165 characters.

It also contains 11 lines.

It is also self-referential.

wow!
'''

# 글자수 공백포함 , 단어 수 , 줄 수 , 유일한 단어 수

def wordcount(filename) :
    counts = {' characters' : 0 , 'words' : 0 , 'lines' : 0}
    unique_words = set()

    for one_line in open(filename) :
        counts['lines'] += 1
        counts['characters'] += len(one_line)
        counts['word'] += len(one_line.split())
        unique_words.update(one_line.split())
    counts['unique words'] = len(unique_words)
    for key, value in counts.items() :
        print(f'{key} : {value}')

wordcount(text)