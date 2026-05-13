'''
6. Automorphic Number Checker

A digital security company designs smart lockers that open only for special self-matching numeric codes. When a user enters a number, the system squares the number and checks whether the result ends with the same digits as the original code. If yes, the locker grants access.

An automorphic number is a number whose square ends with the same number.

Example:
25² = 625

Write a program using loops to check whether the entered number is an Automorphic number.

Input:
25

Output:
Automorphic Number
'''

n = int(input("Enter the number : "))
org = n
s = n**2
count = 0
while n>0 :
    n1 = n%10
    s1 = s%10
    if n1 == s1:
        count += 1
    else:
        count = count
    n = n//10
    s = s//10

if count == len(str(org)):
    print("Automorphic Number")
else:
    print("Not Automorphic Number")



  