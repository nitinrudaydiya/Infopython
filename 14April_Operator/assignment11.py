'''
Assignment 11: Expression Evaluation

A billing system applies nested calculations with discounts and extra charges using brackets and unary operators.

Input:
50 + (10 * (+(2**3))) / 4 - (-6 % 4)
'''

x = 50 + (10 * (+(2**3))) / 4 - (-6 % 4)

print(x)


'''
50 + (10 * (+(2**3))) / 4 - (-6 % 4)
50 +(10 * (+8))/4 - 2
50+80/4-2
50+20.0-2
70.0-2
68

'''