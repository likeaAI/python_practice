




with open('C:\\Users\\crid2\\python_01.txt' , 'r' , encoding='utf-8') as f :
    text01 = f.read()



def read_count() :
    words = text01.split()
    line_count = text01.split(sep='\n')

    char = len(list(text01))
    words_count = len(set(words))
    total_words = len(words)



