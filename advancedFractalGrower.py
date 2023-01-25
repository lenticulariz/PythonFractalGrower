from time import *
from turtle import *
#--SETUP
title("Advanced Fractal Generator")
Screen().bgcolor(0, 0, 0)
Screen().delay(0)
pencolor(1, 1, 1)

speed(0)
shape("turtle")
pensize(3)

left(90)

#--START
axiom = '-'
zoomLevel = 5
angle = 90

rule1A, rule1B = "-", "--+F"
rule2A, rule2B = "++F-", "F-"

#config read
def turtlRead(procAX):
    for char in procAX:

        if char == '-':
            right(angle)
        elif char == '+':
            left(angle)
        elif char == 'F':
            forward(zoomLevel)

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
        pencolor(0+i/iterations, 0+i/iterations, 1-i/iterations)

        print(f"{i+2} {gT}")
        turtlRead(gT)
        sleep(0.25)

growText(20, axiom)

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