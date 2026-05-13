'''
9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime
'''


n = input()

even = 0
odd = 0

for i in n:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1

diff = abs(even - odd)

print("Even Count =", even)
print("Odd Count =", odd)
print("Difference =", diff)

if diff <= 1:
    print("Not Prime")
else:
    count = 0
    for i in range(2, int(diff**0.5)+1):
        if diff % i == 0:
            count += 1
            break
    
    if count == 0:
        print("Prime")
    else:
        print("Not Prime")