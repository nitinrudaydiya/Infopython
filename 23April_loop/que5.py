'''
5. Palindrome Check
A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to **check whether a given number is a palindrome using loops**.

Input: 121
Output: Palindrome
'''

num = int(input("Enter the number = "))
org = num 
pal = 0

while num>0 :
    rem = num%10
    pal = (pal*10) +rem
    num//=10

if org == pal :
    print("Palindrome")
else:
    print("Not Palindrome")


