'''
4. Reverse a Number
A security system stores OTP codes in reverse format for encryption to increase data safety. Reversing a number means extracting digits and rebuilding it in reverse order.
Write a program to **reverse a given integer using loops**.

Input: 1234
Output: 4321
'''
#Wrong 
'''i = int(input("Enter the number = "))

while i > 0 :
    rem = i%10
    print(rem,end="")
    i//=10


#Different method Correct method to find Reverse

n = int(input("Enter the number = "))
rev = 0

while n > 0 :
    rem = n %10
    rev = rev*10+rem
    n//=10

print("Reverse Number is " , rev)'''


#using For

n1 = input("Enter the number ")
rev = ""

for d in n1 :
    rev = d +rev

print("Reversed number " , rev)


# input in integer 