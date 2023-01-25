# PythonFractalGrower
This is a python script designed to grow fractals!

It works via a system based off the L-system. Where you assign a starting axiom, then apply a set of rules to it

For example:
axiom: "A"
ruleset "A" -> "AB"

output:
- A
- AB
- ABB
- ABBB
ect.

After using the L-system to grow letters, you can convert it to grow freactals with turtle. By having it read the output string for each iteration, it can decide what to do depend on the selected character.

Ex:
A - turn right 90, B - turn left 90

character LIB: -+FG/*[]_&

  -, turns the turtle right by a specified amount (angle)
  
  +. turns the turtle left  by a specified amount (angle)
  
  F, puts the turtle forward
  
  G, puts the turtle backward
  
  /, turns the turtle right by (angle^2)
  
  *, turns the turtle left by (angle^2)
  
  [, if the turtle has turned above a specified threshold (i), then it turns the turtle right by that same amount. It also moves the turtle backward by the amount moved (mI)
  
  ], if the turtle has turned above a specified threshold (i), then it turns the turtle left by that same amount. It also moves the turtle forward by the amount moved (mI)
  
  _, a blank character, can be used for patterns. Does nothing to the turtle
  
  &, returns and stops all action further up the axiom level (axiom^i)

