'''
3. Composite Number Detector

A product testing company labels batch numbers as risky if they have more than two factors. Such numbers are known as composite numbers and indicate repeated grouping patterns.

The quality control officer enters a batch number, and the software checks whether it is Composite or Not.

Write a program to check whether a number is Composite or Not.

Input:
12

Output:
Composite Number

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
    
    if num > 1 and count == 0:
        print("Next Prime =", num)
        break