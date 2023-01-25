from time import *
from turtle import *
#--SETUP
def setup(Title, bgColor, isTurtle):
    title(Title)
    Screen().bgcolor(bgColor)
    Screen().delay(0)
    pencolor(0, 0, 0)
    #penup()

    speed(0)

    if isTurtle:
        shape("turtle")
    pensize(3)

    left(90)
setup("Advanced Fractal Generator", (0, 0, 0), False)

#charLIB: -+FG/*[]_&
#-, turns the turtle right by a specified amount (angle)
#+. turns the turtle left  by a specified amount (angle)
#F, puts the turtle forward
#G, puts the turtle backward
#/, turns the turtle right by (angle^2)
#*, turns the turtle left by (angle^2)
#[, if the turtle has turned above a specified threshold (i), then it turns the turtle right by that same amount. It also moves the turtle backward by the amount moved (mI)
#], if the turtle has turned above a specified threshold (i), then it turns the turtle left by that same amount. It also moves the turtle forward by the amount moved (mI)
#_, a blank character, can be used for patterns. Does nothing to the turtle
#&, returns and stops all action further up the axiom level (axiom^i)

#--START
axiom = '_F'
zoomLevel = 20
angle = 90
threshold = 100

rule1A, rule1B = "_", "__"
rule2A, rule2B = "_______", "G&"

#config read
def turtlRead(procAX):
    i = 0
    mI = 0
    for char in procAX:
        if char == '-':
            right(angle)
            i += angle/10
        
        elif char == '&':
            return
        
        elif char == '+':
            left(angle)
            i -= angle/10
        
        elif char == 'F':
            forward(zoomLevel)
            mI += 5
        
        elif char == 'G':
            backward(zoomLevel)
            mI -= 5
        
        elif char == '/':
            right(angle**2)
            i += angle**2
        
        elif char == '*':
            left(angle**2)
            i -= angle**2
            
        
        elif char == '[':
            if i >= threshold:
                right(i)
                backward(mI*zoomLevel)
        
        elif char == ']':
            if i >= threshold:
                left(i)
                forward(mI*zoomLevel)
        
        elif char == '_':
            pass



#__shell__
def grow(textToGrow, replaceFind, replaceWith):
    return textToGrow.replace(replaceFind, replaceWith)

def growText(iterations, ax):
    gT = ax
    print("1 " + gT)
    
    for i in range(iterations):
        gT = grow(gT, rule1A, rule1B)

        print(f"{i+2} {gT}")
        turtlRead(gT)
        sleep(0.25)
        gT = grow(gT, rule2A, rule2B)
        pencolor(1-i/iterations, 0+i/iterations, 0+i/iterations)

        print(f"{i+2} {gT}")
        turtlRead(gT)
        sleep(0.25)

growText(60, axiom)

input()

mainloop()

#SAVED FRACTALS---

#Spiral curve
#Axiom: 0
#RULESET:
#gT = grow(gT, '0', '0012')
#gT = grow(gT, '1120', '20')
#alphabet: 0 - turn right | 1 - turn left | 2 - forward

#Wave fractal
#Axiom: A
#RULESET:
#gT = grow(gT, 'B', 'BB')
#gT = grow(gT, 'A', 'B[A]A')
#if char == ']': right(angle)         
#elif char == '[': left(angle)         
#elif char == 'A': forward(zoomLevel)          
#elif char == 'B': forward(zoomLevel) 

#Trangle fractal
#Angle: 120
#Axiom: F
#RULESET:
#rule1A, rule1B = "F", "F-F+FG-G+G"
#rule2A, rule2B = "FG", "G+F"

#if char == '-': right(angle)           
#elif char == '+': left(angle)           
#elif char == 'F': forward(zoomLevel)           
#elif char == 'G': backward(zoomLevel)
