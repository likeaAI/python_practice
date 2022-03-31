




with open('C:\\Users\\crid2\\python_01.txt' , 'r' , encoding='utf-8') as f :
    text01 = f.read()


# 파일을 4번 읽어서 하는 방법.. -_
def read_count() :
    words = text01.split()
    line_count = text01.split(sep='\n')

    char = len(list(text01))
    words_count = len(set(words))
    total_words = len(words)




# 파일을 한번만 읽고 처리하는 방법
def wordcount() :
    counts = { 'characters' : 0,
               'words' : 0 ,
                'lines' : 0 ,

    }
    unique_word = set()


    for one_line in text01 :
        counts['lines'] += 1
        counts['characters'] += len(one_line)
        counts['words'] += len(one_line.split())
        unique_word.update(one_line.split())
    counts['unique_words'] = len(unique_word)
    for key, value in counts.items() :
        print(f'{key} : {value}')

wordcount()
