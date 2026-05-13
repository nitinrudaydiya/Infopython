'''
5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3
'''


n = int(input())

num = n

while True:
    num += 1
    count = 0
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            count += 1
            break
    
    if count == 0:
        print("Next Prime ID =", num)
        print("Gap =", num - n)
        break