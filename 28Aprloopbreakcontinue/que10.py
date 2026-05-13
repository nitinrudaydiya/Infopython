'''
10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime
'''



n = input()

zero = 0
s = 0
smallest = int(n[0])

for i in n:
    digit = int(i)
    
    if digit == 0:
        zero += 1
    
    s += digit
    
    if digit < smallest:
        smallest = digit

final = (zero + s) * smallest

print("Zero Count =", zero)
print("Sum =", s)
print("Smallest Digit =", smallest)
print("Final Result =", final)

if final <= 1:
    print("Not Prime")
else:
    count = 0
    for i in range(2, int(final**0.5)+1):
        if final % i == 0:
            count += 1
            break
    
    if count == 0:
        print("Prime")
    else:
        print("Not Prime")