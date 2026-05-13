'''
Assignment 16: Expression Evaluation

A performance evaluation system calculates final score using grouped operations, exponent, division, and unary adjustments.

Input:
45 + (15 * (2**2)) - (20 / (+(5))) + (-(7 % 3))

'''

z = 45 + (15 * (2**2)) - (20 / (+(5))) + (-(7 % 3))
print(z)

'''
45 + (15 * (2**2)) - (20 / (+(5))) + (-(7 % 3))
45+(15*4)-(20/(+5))+(-1)
45+60-4.0-1
105-4.0-1
101.0-1
100.0

'''