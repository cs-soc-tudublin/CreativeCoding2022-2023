def q1():
    for i in range(0,11):
        print(i)

def q2():
    while True:
        if input("What is your favourite food?") == "burgers":
            break

def q3():
    primes = 0
    for i in range(2,101):
        facts = 0
        for j in range(1, i + 1):
            if i % j == 0:
                facts += 1
        if facts == 2:
            primes += 1

    print(primes)

def q4():
    list1 = [0,11,15,67,22,54]
    list2 = []

    for i in list1:
        list2.append(i ** 2)

def q5():
    x = "CS++ is very cool".split()
    for i in x:
        print(i)

def q6():
    """
    i[x] increments value at x
    d[x] decrements value at x
    s[x] squares value at x
    o outputs all values in memory
"""

    # [1, 2, 4, 16]


    program = "i1 o"

    mem = [0,0,0,0]

    instructions = program.split()


    for op in instructions:
        inst = op[0]
        if inst == 'i':
            index = int(op[1]) - 1
            mem[index] += 1
        elif inst == 'd':
            index = int(op[1]) - 1
            mem[index] -= 1
        elif inst == 's':
            index = int(op[1]) - 1
            mem[index] *= mem[index]
        elif inst == 'o':
            print(mem)


def main():
    funcs = [q1,q2,q3,q4,q5,q6]

    for x in funcs:
        x()
        print("\n\n")

if __name__ == "__main__":
    main()
