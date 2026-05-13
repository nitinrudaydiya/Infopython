'''
1.Digit Product Analyzer System

A data analytics company studies patterns in numeric transaction IDs to detect hidden behaviors.

For every entered number, the system analyzes relationships between its digits.

Write a program to:

Find the product of every pair of adjacent digits
Display all the products
Find the sum of all these products
Find the smallest product value
If the sum of products is divisible by the total number of digits, print Stable Number
Otherwise print Unstable Number

Use loops wherever required.

Input:
57294

Output:
Products: 35 14 18 36
Sum = 103
Smallest = 14
Unstable Number
'''

num= input("Enter the number : ")
pro = 1
sum = 0
i=0
small=int(num)
print("Products: ",end="")
while i<(len(num)-1):
    n1=int(num[i])
    n2=int(num[i+1])
    pro=n1*n2
    
    if small<pro :
       small=small
    else:
       small = pro
    print(pro,end=" ")
    sum += pro 
    i+=1
print(f"\n{sum}")
print(f"Smallest = {small}")

if sum == len(num):
    print("Stable Number")
else:
    print("Unstable Number")





'''while num>10:
    rem=num%10
    num=num//10
    rem1=num%10
    pro=rem*rem1
    print(pro)'''
    
