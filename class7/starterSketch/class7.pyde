from Classes import *

def settings():
    size(500,500)
    
game = None

def setup():
    colorMode(HSB)
    global  game
    textSize(100)
    background(0)
    game = Game()
    pass

    
def draw():
    global game
    game.drawGame()
    game.checkCollisions()
    
def keyPressed():
    global game
    fill(0)
    rect(0,0, 10, height)
    rect(width - 10, 0, 10, height)
    print(frameCount,"Move now", key)
    game.handleInput(key)
    print(game.paddleA.y, game.paddleB.y)
