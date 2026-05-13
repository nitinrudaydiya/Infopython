'''
1. Largest Digit in Number
A cybersecurity company checks numeric passwords used in smart lockers. To identify password strength, the system finds the highest digit present in the entered password. Higher digits indicate stronger variation in the password pattern.
Write a program to find the largest digit in a number using loops.

Input:
57294

Output:
Largest Digit = 9

'''
'''
n = int(input("Enter the number = "))
largest = 0
for i in str(n):
    if int(i) > largest:
        largest = int(i)

print(f"Largest Digit = {largest}")
'''

n1 = int(input("Enter the number n1 = "))
largest = 0
while n1 > 0 :
    rem = n1%10
    if rem > largest:
        largest = rem 
    n1//=10

print(f"Largest digit = {largest}")

 