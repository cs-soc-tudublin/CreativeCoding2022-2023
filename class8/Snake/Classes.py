STEP_SIZE = 10

class Node:
    def __init__(self, x, y, dir,isHead=False, isFood=False):
        pass

    def push(self):
        pass 
    def move(self):
        pass 
    def chDir(self):
        pass
    def checkCols(self, foodX, foodY):
        pass 

    def render(self):
        if self.isHead == True:
            fill(0,0,255)
        else:
            fill((self.col + frameCount) % 255, 255,255)

        circle(self.x, self.y, STEP_SIZE)
        if self.next != None:
            self.next.render()
        
