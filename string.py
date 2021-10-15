word_one = "word!"
word_two = "Hello"

word_one, word_two = word_two, word_one

print(str(word_one) + ', ' + str(word_two))

def retro():
    return 'a', 'b', 'c'
first, second, third = retro()
  
print(first, second, third)
