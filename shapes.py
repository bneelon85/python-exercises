from turtle import *
def Circle(rad,filL ,col):
    color(col,col)
    if(filL == True):
        begin_fill()
        circle(rad)
        end_fill()
    else:
        circle(rad)
    
def Hexagon(side, filL ,col):
    color(col,col)
    if(filL == True):
        begin_fill()
        for i in range(6):
            forward(side)
            left(60)
        end_fill()
    else:
        for i in range(6):
            forward(side)
            left(60)
    
        
def Square(side,  filL,col):
    color(col,col)
    if(filL == True):
        begin_fill()
        for i in range(4):
            forward(side)
            left(90)
        end_fill()
    else:
        for i in range(4):
            forward(side)
            left(90)

    
def EqTriangle(side,  filL,col):
    color(col,col)
    if(filL == True):
        begin_fill()
        for i in range(3):
            forward(side)
            left(120)
        end_fill()
    else:
        for i in range(3):
            forward(side)
            left(120)
    
def Star(side,  filL,col):
    color(col,col)
    if(filL == True):
        begin_fill()
        for i in range(5):
            forward(side)
            left(144)
        end_fill()
    else:
        for i in range(5):
            forward(side)
            left(144)
    
def Pentagon(side,  filL,col):
    color(col,col)
    if(filL == True):
        begin_fill()
        for i in range(5):
            forward(side)
            left(72)
        end_fill()
    else:
        for i in range(5):
            forward(side)
            left(72)
    
def Octagon(side,  filL,col):
    color(col,col)
    if(filL == True):
        begin_fill()
        for i in range(8):
            forward(side)
            left(45)
        end_fill()
    else:
        for i in range(8):
            forward(side)
            left(45)

