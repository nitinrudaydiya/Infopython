'''
3. First Digit of Number
A university receives thousands of application IDs. The first digit of each ID represents the department code, so the admission software must read the first digit quickly.
Write a program to find the first digit of a number using loops.

Input:
53892

Output:
First Digit = 5
'''

i = int(input("Enter the Number = "))

while i > 10:
    rem = i%10
    i//=10

print(f"First Digit = {i}")