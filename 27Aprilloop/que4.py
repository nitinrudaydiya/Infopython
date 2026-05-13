'''
4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number
'''

n = int(input("Enter number : "))
n1 = n
sum = 0
for i in str(n):
    fact = 1
    
    for j in range(1,int(i)+1):
        fact = fact*int(j)
    sum += fact
    print(fact)

print(sum)
if n==sum:
    print("Strong Number")



