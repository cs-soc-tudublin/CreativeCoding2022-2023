from Classes import *

def settings():
    size(500,500)
    
#recursion limit is 999
def setup():
    colorMode(HSB)
    pass

snek = Node(250, 250, 'a',True)
fod1 = Node((random(0,500)//STEP_SIZE) * STEP_SIZE, (random(0,500)//STEP_SIZE) * STEP_SIZE, 'b', False, True)


def draw():
    global fod1
    global snek
    background(0)
    snek.render()
    fod1.render()
    if frameCount % STEP_SIZE == 0:
        snek.move()
        res = snek.checkCols(fod1.x, fod1.y)
        if res == True:
            snek.push()
            fod1 = Node((random(0,500)//STEP_SIZE) * STEP_SIZE, (random(0,500)//STEP_SIZE) * STEP_SIZE, 'b', False, True)
        elif res == "ouch":
            snek = None
            fod1 = None
            print("Game over BOZO")    
    
def keyPressed():
    snek.dir = key
    snek.chDir()

    
