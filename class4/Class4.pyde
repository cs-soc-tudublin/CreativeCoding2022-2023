def settings():
    size(1000,1000)

dAng = 0

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
    count = 20
    gapX = width/count
    gapY = height/count
    
    for i in range(0,count):
        fill(map(i, 0, count, 0,255),255,255)
        square(gapX * i, gapY * i, min(gapX, gapY))
        square(width - (gapX * (i + 1)), gapY * i, min(gapX, gapY))
    
def p3():
    colorMode(HSB)
    global dAng
    
    count = 50
    line(0,height/2,width,height/2)
    ang =  TAU / count
    ang += dAng
    for i in range((count + 1)/2):
        col = map(i, 0,(count + 1)/2, 0,150)
        fill((col % 150) + 27, 255,255)
        stroke((col % 150) + 27, 255,255)
        pX = i * width/count
        pY = height/2 + (height/2 * sin(ang * i)) -10
        pX2 = (i + 1) * width/count
        pY2 = height/2 + (height/2 * sin(ang * (i + 1)))
        line(width - pX, height/2,pX, pY)
        line(pX, height/2, width - pX, height - pY)
        circle(width - pX, height - pY, 10)
        circle(pX, pY, 10)
        
    dAng += 0.0005
        
    pass

count = 0

def setup():
    pass 
def draw():
    global count
    
    if frameCount % 60 == 0:
        count += 1    
    
    count = count % 3
    
    background(0)
    if count == 0:
        p1()
    if count == 1:
        p2()
    if count == 2:
        p3()
    saveFrame("output.png")
    
