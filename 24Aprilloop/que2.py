'''
2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2
'''
'''
s = int(input("Enter the number = "))
smallest = 0

for i in str(s):
    if int(i) < smallest :
        smallest = int(i)


print(f"Smallest Digit = {smallest}")
'''

n1 = int(input("Enter the number n1 = "))
smallest = 0
while n1 > 0 :
    rem = n1%10
    if rem < smallest:
        smallest = rem 
    n1//=10

print(f"Largest digit = {smallest}")
