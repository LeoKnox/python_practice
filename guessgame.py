import random

answer = random.randint(0, 100)
guess = input('Enter a guess:')
guess = int(guess)

while guess != answer:
    guess = input(str(answer) + 'Enter another guess: ')
    guess = int(guess)
print ("win")
