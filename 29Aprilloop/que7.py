'''
7.
 Alternate Digit Prime Checker

A math lab adds alternate digits from right side.

Write a program to:

- Find sum of alternate digits
- Check whether sum is Prime or Not

Input:
12345

Output:
Alternate Sum = 9
Not Prime
'''

num = int(input("Enter number: "))

alt_sum = 0
take = True   # to pick alternate digits

# process from right side
while num > 0:
    digit = num % 10
    if take:
        alt_sum += digit
    take = not take
    num //= 10

print("Alternate Sum =", alt_sum)

# check prime using for-else
if alt_sum < 2:
    print("Not Prime")
else:
    for i in range(2, alt_sum):
        if alt_sum % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")