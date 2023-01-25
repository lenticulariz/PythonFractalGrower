from advancedFractalGrower import *
from turtle import mainloop

setup("fractalExample", (0, 0, 0), False)

axiom = "F"
zoomLevel = 20
angle = 90
threshold = 100

rule1A, rule1B = "F", "F+"
rule2A, rule2B = "F", "F"

growText(20, axiom)

mainloop()