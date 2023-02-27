"""
STARTER CODE FOR CREATIVE CODING 6
"""

def head(xs):
    return xs[0]

def tail(xs):
    return xs[1::1]


def flatten(xs):
    newList = []
    for x in xs:
        if isinstance(x, list):
            for y in x:
                newList.append(y)
        else:
            newList.append(x)
    return newList

def cons(a, b):
   return flatten([a,b]) 

#----------------------------------------------------
#YOUR CODE HERE


#Question 1
def fact(x):
    pass

#Question 2
def count(xs):
    pass

#Question 3
def sumList(xs):
    pass

#Question 4
def fib(n):
    pass

#Question 5
def take(xs, n):
    pass

#Question 6
def drop(xs, n):
    pass

#----------------------------------------------------

"""
EXAMPLES
"""

def printNums(x):
    print(x)
    if x <= 1:
        return
    printNums(x - 1)

def printList(xs):
    print(head(xs))

    if len(xs) == 1:
        return

    printList(tail(xs))
