# Rounding

Simple function to round numbers away from 0:
(12.5 -> 13, -12.5 -> -13)

1. You can run rounding_interactive.py to have interactive mode:
python -m rounding_interactive

2. You can run:
python -m rounding 12.55 1 #The result is: Rounding number 12.55 with precision 1: 12.6

3. You can import function like this:
from rounding import rd
rd (12.55) #returns '13', or
rd (12.55, 1) #return '12.6'
