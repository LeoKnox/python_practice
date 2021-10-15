from collections import Counter

word_one = "word!"
word_two = "Hello"

word_one, word_two = word_two, word_one

print(str(word_one) + ', ' + str(word_two))

def retro():
    return 'a', 'b', 'c'
first, second, third = retro()
  
print(first, second, third)


def find_anagram(first_str, second_str):
     return Counter(first_str) == Counter(second_str)
  
def find_anagram(first_str, second_str): 
    return sorted(first_str) == sorted(second_str) 
  
print(find_anagram('taco', 'coat'))
print(find_anagram('bleak', 'brake'))  
