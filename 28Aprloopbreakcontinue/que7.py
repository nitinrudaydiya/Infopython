'''
7.
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number
'''

n = input("Enter the num")

s = 0
for i in n:
    s += int(i)

print("Sum =", s)

if s <= 1:
    print("Normal Number")
else:
    count = 0
    for i in range(2, int(s**0.5)+1):
        if s % i == 0:
            count += 1
            break
    
    if count == 0:
        print("Lucky Number")
    else:
        print("Normal Number")