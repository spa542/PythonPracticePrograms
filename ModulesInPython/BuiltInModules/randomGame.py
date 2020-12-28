# Random Game Example

from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        guess = int(input('Guess a number 1-10: '))
        if 1 < guess < 11:
            if guess == answer:
                print('You are a genius!')
                break
        else:
            print('Hey bozo, I said 1-10')
    except ValueError:
        print('Please enter a valid number')
