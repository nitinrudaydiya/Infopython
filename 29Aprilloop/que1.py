'''
1. Triple Operation Prime Verification System

A cybersecurity company generates a security score from entered access code.

Write a program to:

- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime

Input:
4215

Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime

'''

n = input("Enter the number : ")
rev = ""
sum = 0
for i in n :
    rev = i + rev
    sum += int(i)
rev = int(rev)
n = int(n)
dif = n - rev
dif = abs(dif)
final = sum + dif



print("Sum of Digits =",sum)
print("Reverse =" , rev)
print("Difference =",dif)
print("Final Result =",final)

if final <=1 :
    print("Not Prime")
else :
    for i in range(2,int(final**0.5)+1):
        if final % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")