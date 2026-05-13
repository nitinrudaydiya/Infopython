'''
4.Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number
'''

n = input("Enter the number : ")
sum = 0
mul = 1

for i in n :
    m = int(i)
    sum += m
    mul *= m

if sum == mul :
    print("Spy Number")
else:
    print("Not Spy Number")