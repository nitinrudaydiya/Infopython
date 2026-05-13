'''
5.Number Stability Analyzer

A science lab studies whether digits are in increasing order.

Write a program using for-else loop:

- If every next digit is greater than previous print Stable Number
- Else Unstable Number

Input:
12359

Output:
Stable Number
'''

num = input("Enter number: ")

prev = ""

for digit in num:
    if prev != "" and digit <= prev:
        print("Unstable Number")
        break
    prev = digit
else:
    print("Stable Number")