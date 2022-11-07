#!/bin/python3

def q1():
    
    def sayHi():
        print("Hello CS++")
    
    sayHi()

def q2():
    def printString(strang):
        print(strang)

    printString("Hello")

def q3():
    
    def addTwo(a,b):
        return a+b

    print(addTwo(1,2))

def q4():
    
    def addTwo(a,b,op):
        if(op == '+'): 
            return a+b
        if(op == '-'): 
            return a-b
        if(op == '*'): 
            return a * b
        if(op == '/'): 
            return a / b

    print(addTwo(1,2, '-'))

def q5():

    def checkIn(lst, num):
        return num in lst

    print(checkIn([1,1,1,1,2,2,3,4,5,6,7,7],5))
    
def q6():

    def addTwo(a,b):
        return a + b

    def subTwo(a,b):
        return a - b

    def mulTwo(a,b):
        return a * b

    def divTwo(a,b):
        return a / b

    def powTwo(a,b):
        return a ** b

    def floorTwo(a,b):
        return a // b

    def modTwo(a,b):
        return a % b

    lst = [addTwo, subTwo, mulTwo, divTwo, powTwo, floorTwo, modTwo]

    for i in lst:
        a = 50
        b = 5

        print(i(a, b))

if __name__ == "__main__":
    x = [q1,q2, q3, q4, q5, q6]
    for y in x:
        y()
        print()
