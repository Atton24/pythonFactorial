#created by Daniel Thomas
#created in Python 2.7.11
#last updated 3/11/19


import string
import random

#recursive factorial limited by recursion depth
def factorial(num):
    if num == 1:
        return num
    return num * factorial(num-1)

#iterative factorial
def loopFactorial(num):
    temp = 1
    index = 1
    while index != num+1:
        temp *= index
        index += 1
    return temp


attempts = 0
myNum = None

#attempts to get an integer >= 0 from the user
while type(myNum) != int or myNum < 0:
    try:
        if attempts < 10:
            myNum = int(raw_input("Type a positive integer: "))
        else:
            myNum = int(raw_input("PLEASE type a positive integer :) : "))
    except:
        None
    if type(myNum) != int or myNum < 0:
        if attempts == 0:
            print 'Type a positive integer please'
            print
        elif attempts < 5:
            print 'POSITIVE INTEGER' + '!' * attempts
            print
        else:
            temp = ''
            for i in range(random.randint(5, 15)):
                temp += random.choice(string.letters)
            print temp + "!!!!!!"
            print
    attempts += 1

print "Factorial of " + str(myNum) + " is: " + str(loopFactorial(myNum))
