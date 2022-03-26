# list comprehesin 내포 연습


test01 = [x*x for x in range(5)]
print(test01)
# 0,1, 4, 9 , 16

test02 = {x:x*2 for x in range(5)}
print(test02)

test03 = {x*x for x in range(5)}
print(test03)


test04 = [x*x
          for x in range(5)
          if x%2 ]
print(test04)


test05 = [(x,y) for x in range(5) if x%2 \
          for y in range(5) if y%3]

print(test05)

words = 'this is a bunch of words.'.split()
x = map(len, words)
print(sum(x))

def is_a_long_word(one_word) :
    return len(one_word) > 4
x = filter(is_a_long_word, words)
print(''.join(x))



