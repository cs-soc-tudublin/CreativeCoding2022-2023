def settings():
    size(500,500)
    
def setup():
    colorMode(HSB)
    
SQUARE_MAX = 1    

def recSquare(depth):
    pass

TREE_MAX = 1

def recTree(x, y, ang, depth):
    pass

count = 0

def draw():
	
    colorMode(HSB)
    global count
    background(0)
    translate(width/2, height/2)
    if frameCount % 120 == 0:
        count += 1
    
    #uncomment this line to manually pick each drawing
    #count = 0
    
	#cycling between the sketches every 2 seconds
    if count % 2 == 0:
        recSquare(SQUARE_MAX)
    if count % 2 == 1:
        recTree(0,height/3,0,TREE_MAX)
    
