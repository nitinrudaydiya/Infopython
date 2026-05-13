'''
9.
Abundant Number Detector

A financial system analyzes surplus numbers.

An Abundant Number:
Sum of proper factors > number

Write a program to check Abundant Number.

Input:
12

Output:
Abundant Number

'''

n = int(input("Enter the number : "))
fsum = 0

for i in range(1,n):
    if n%i == 0:
        fsum+=i
    else:
        fsum = fsum

if fsum > n :
    print("Abundant Number")
else:
    print("Not an Abundant Number")

