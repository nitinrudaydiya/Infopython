'''
8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime
'''

n = input()

largest = -1
smallest = 9

for ch in n:
    digit = int(ch)
    
    if digit > largest:
        largest = digit
    
    if digit < smallest:
        smallest = digit

s = largest + smallest

print("Largest =", largest)
print("Smallest =", smallest)
print("Sum =", s)

# Prime check (√n)
if s <= 1:
    print("Not Prime")
else:
    count = 0
    
    for i in range(2, int(s**0.5) + 1):
        if s % i == 0:
            count += 1
            break
    
    if count == 0:
        print("Prime")
    else:
        print("Not Prime")