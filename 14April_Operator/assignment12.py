'''
Assignment 12: Expression Evaluation

A gaming score system calculates bonus points using exponent and applies penalties using unary negative values and brackets.

Input:
100 - (20 * (3**2)) + (40 / (+5)) - (-3)

---

'''


x = 100 - (20 * (3**2)) + (40 / (+5)) - (-3)
print(x)


'''
100 - (20 * (3**2)) + (40 / (+5)) - (-3)
100 - (20 * 9) + 8.0 + 3 
100 - 180 + 8.0 +3
-80+8.0+3
-72.0+3
-69.0
'''