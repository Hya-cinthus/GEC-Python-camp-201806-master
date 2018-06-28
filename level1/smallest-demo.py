# smallest-exercise.py
# define a function that returns the smallest number in a given list
# use for loop
# complete the code

#theList = [4,3,2,7,1,10] #the list we'll test our function with
theList = [90,124,42123,234,23,65,123,32,40]

def smallest(myList): #myList is a general list. part of the recipe.
    minimum = myList[0]
    for element in myList:
        if(minimum > element):
            minimum = element
    return minimum


def maximum(myList):
    maximum = myList[0]
    for element in myList:
        if(maximum < element):
            maximum = element
    return maximum

print("minimum:",smallest(theList),"\nmaximum:",maximum(theList))
