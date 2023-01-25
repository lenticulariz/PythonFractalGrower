# PythonFractalGrower
This is a python script designed to grow fractals!

It works via the L-system. Where you assign a starting axiom, then apply a set of rules to it

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
