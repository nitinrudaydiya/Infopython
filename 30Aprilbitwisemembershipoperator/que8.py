'''
8.
Trimorphic Number Analyzer

A coding system checks cube-based patterns.

A Trimorphic Number:
Cube of number ends with the same number.

Example:
4³ = 64

Write a program to check Trimorphic Number.

Input:
4

Output:
Trimorphic Number
'''

n = int(input("Enter the number : "))
m = n
cube = n**3

count = 0
while cube>0:
    rem1 = n%10
    rem2 = cube%10
    n= n//10
    cube = cube//10
    if rem1 == rem2 :
        count+=1
    else:
        count=count

if count==len(str(m)):
    print("Trimorphic Number")
else:
    print("Not An Trimorphic Number")

