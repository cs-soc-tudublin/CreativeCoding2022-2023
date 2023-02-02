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
    funcs = []
    funcs.append(lambda a,b : a + b)
    funcs.append(lambda a,b : a - b)
    funcs.append(lambda a,b : a / b)
    funcs.append(lambda a,b : a * b)
    funcs.append(lambda a,b : a ** b)
    funcs.append(lambda a,b : a % b)

    for x in funcs:
        print(x(2,3))

if __name__ == "__main__":
    x = [q1,q2, q3, q4, q5, q6]
    for y in x:
        y()
        print()
