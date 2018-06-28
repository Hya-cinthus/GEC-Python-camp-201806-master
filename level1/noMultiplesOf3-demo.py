#noMultiplesOf3.py
#write a program that prints out all numbers
#from 0 to 100
#that are NOT multiples of 3.

#modulo operator: the remainder of a division
#print(3%3) #gives us 0
#print(4%3) #gives us 1
#print(5%3) #gives us 2
#print(6%3) #gives us 0 (6 is divisible by 3)

x = 0
for x in range(101):
    if (x%3!=0):
        print(x)
