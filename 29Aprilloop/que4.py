'''
4.Unique Digit Security Scanner

A smart locker accepts only numbers whose all digits are unique.

Write a program using for-else loop to:

- Check every digit
- If any repeated digit found reject
- Else accept

Input:
57294

Output:
Valid Unique Code
'''

num = input("Enter code: ")
seen = ""

for digit in num:
    if digit in seen:
        print("Invalid Code")
        break
    else:
        seen += digit
else:
    print("Valid Unique Code")