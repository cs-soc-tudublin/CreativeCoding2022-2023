import sys

STACK_MAX = 100
STACK_PTR = 0

STACK = []

for _ in range(STACK_MAX):
    STACK.append(0)

counter = 0
def iota():
    global counter
    counter += 1
    return counter

OP_PUSH = iota()
OP_POP= iota()
OP_ADD= iota()
OP_SUB= iota()
OP_DIV= iota()
OP_MUL= iota()
OP_PRINT= iota()
OP_APRINT= iota()

def Exec(inst):
    global STACK
    global STACK_PTR
    global STACK_MAX
    if inst[0] == OP_PUSH:
        if STACK_PTR != STACK_MAX:
            STACK_PTR += 1
            STACK[STACK_PTR] = inst[1]

    if inst[0] == OP_POP:
        if STACK_PTR != 0:
            t = STACK[STACK_PTR]
            STACK_PTR -= 1
            return t

    if inst[0] == OP_ADD:
        a = Exec((OP_POP,))
        b = Exec((OP_POP,))
        Exec((OP_PUSH, a + b))

    if inst[0] == OP_SUB:
        a = Exec((OP_POP,))
        b = Exec((OP_POP,))
        Exec((OP_PUSH, a - b))


    if inst[0] == OP_DIV:
        a = Exec((OP_POP,))
        b = Exec((OP_POP,))
        Exec((OP_PUSH, a / b))

    if inst[0] == OP_MUL:
        a = Exec((OP_POP,))
        b = Exec((OP_POP,))
        Exec((OP_PUSH, a * b))

    if inst[0] == OP_PRINT:
        print(STACK[STACK_PTR])

    if inst[0] == OP_APRINT:
        print(STACK)

def Compile(s):
    code = s.split()
    if code[0] == "push":
        num = int(code[1])
        return (OP_PUSH, num)
    if code[0] == "pop":
        return (OP_POP,)
    if code[0] == "add":
        return (OP_ADD,)
    if code[0] == "sub":
        return (OP_SUB,)
    if code[0] == "div":
        return (OP_DIV,)
    if code[0] == "mul":
        return (OP_MUL,)
    if code[0] == "print":
        return (OP_PRINT,)
    if code[0] == "aprint":
        return (OP_APRINT,)

def interactive():
    s = 0
    while s != "exit":
        s = input(">>>")
        Exec(Compile(s)) 

def fileC(s):
    fp = open(s, "r")
    source = fp.readlines()
    program = []
    for x in source:
        program.append(Compile(x))
    for x in program:
        Exec(x)

def main():
    if len(sys.argv) == 1:
        interactive()
    if len(sys.argv) == 2:
        fileC(sys.argv[1])

if __name__ == "__main__":
    main()
