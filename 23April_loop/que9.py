'''
**9. Check All Digits Are Even**
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to **check whether all digits of a number are even using loops**.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even
'''

num = int(input("Enter the num = "))
count = 0
while num > 0:
    rem = num%10
    if rem%2!=0:
       count+=1
    num//=10

if count > 0:
    print("Not All Even")
else:
    print("All Even")