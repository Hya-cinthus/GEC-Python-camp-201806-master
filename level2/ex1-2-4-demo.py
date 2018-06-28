#Ex. 1
    #write a function that tests whether a number is prime or not.
    #hint: use the modulo operator (%)
    #hint: n=1 and n=2 are separate cases. 1 is not prime and 2 is prime.
'''
def isprime(n):
    judge = True
    if(n==1):
        judge = False
    if(n==2):
        judge = True
    for i in range(2,int(n ** 0.5)):
        if(n % i == 0):
            judge = False
            break
    return judge
'''

#Ex. 2
    #write a function that computes the Least Common Multiple of two numbers
'''
def lcm(a,b):
    c = (abs(a-b)+a+b)/2 # maximum of the two
    i=1
    result = c  # final variable
    while(result%a !=0 or result%b != 0): # stops when lcm obtained
        i=i+1
        result = c*i    # multiples of the larger number
    return result
'''


#Ex. 4
	#fibonacci.py
	#write a function that prints out the first n
	#fibonacci numbers

	#1,1,2,3,5,8,13,21,...
	#f(n) = f(n-1) + f(n-2)
'''
def fibonacci(n):
    result = 0
    if(n==1 or n==2):
        result = 1
    else:
        i=1
        j=1
        for loop in range(n-1):
            k = j
            j = i+j
            i = k
        result = i
    return result
'''       
