def settings():
    size(500,500)

def p1():
    stroke(255)
    lineCount = 20
    cX = width/2
    cY = height/2
    noFill()
    circle(cX,cY, min(width,height)/4)
    circle(cX,cY, min(width,height))
    ang = TAU/lineCount
    
    for i in range(0,lineCount/2):
        pX1 = cX + cX * sin(ang * i)
        pY1 = cY + cY * cos(ang * i)
        pX2 = cX - cX * sin(ang * i)
        pY2 = cY - cY * cos(ang * i)
        line(pX2, pY2, pX1, pY1)
        
        
def p2():
    count = 10
    gapX = width/count
    gapY = height/count
    for i in range(0,count):
        square(gapX * i, gapY * i, min(gapX, gapY))
        square(width - (gapX * (i + 1)), gapY * i, min(gapX, gapY))
    
def p3():
    count = 100
    line(0,height/2,width,height/2)
    ang = TAU / count
    for i in range((count + 1)/2):
        pX = i * width/count
        pY = height/2 + (height/2 * sin(ang * i))
        stroke(255)
        line(width - pX, height/2,pX, pY)
        line(pX, height/2, width - pX, height - pY)
        circle(width - pX, height - pY, 10)
        circle(pX, pY, 10)
        
    pass
    
def draw():
    background(0)
    p3()
    print(frameCount, ": new frame")
    
