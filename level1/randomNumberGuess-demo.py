import random

computerChoice = random.randint(1,100)
win = False #a boolean variable
count = 0

while not(win):
    userChoice = input("what's your guess?")
    try:
        userChoice = int(userChoice)
        count = count + 1
        if(count<=10):
            if(userChoice > computerChoice):
                print("your choice was too high:(")
            elif(userChoice< computerChoice):
                print("your choice was too low:(")
            elif(userChoice == computerChoice):
                print("correct!")
                win = True
                print("you win!")
        else:
            print("Too many guesses!")
            win = True
            print("You lose!")
    except:
        print("Please enter an integer!")
        continue
        print("This won't appear!")


