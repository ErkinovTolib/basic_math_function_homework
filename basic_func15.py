# Create a function called main.
# Create function arguments a and b.
from math import abs
def main(a,b):
# Return the modulus of a and b.
    x = abs(a)
    y = abs(b)
    return x,y
print(main(27,8))