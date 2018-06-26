# randomNumberGues-exercise.py
# write a program to guess the number
# use while loop
# use if-elif
# complete the code

import random

computerChoice = random.randint(1,100)
win = False #a boolean variable

while not(win):
    userChoice = int(input("what's your guess?"))
    

print("you win!")
