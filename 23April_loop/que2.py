'''
2. Factorial of a Number
In project scheduling, tasks are dependent on previous tasks, and the total number of ways to arrange them is calculated using factorial. Factorial of a number n is the product of all numbers from 1 to n.
Write a program to calculate the **factorial of a given number using loops**.

Input: n = 5
Output: Total Ways = 120

'''
n = int(input("Enter n number = "))
fact = 1 
for i in range(1,n+1):
    fact*=i

print(F"Total Ways = {fact}")

#Using while loop 

f = 1 
while n>0 :
    f = f*n
    n=n-1

print("Factorial of n no. ",f)

#Using math module 

n1 = int(input("Enter n1 number = "))


import math 
print("Factorial of n no. ",math.factorial(n1))


