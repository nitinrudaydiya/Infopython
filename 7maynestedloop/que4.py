'''
4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407

'''


n = int(input("Enter starting number: "))
m = int(input("Enter ending number: "))
print("Armstrong Numbers are: ")
for i in range(n,m+1):
    x = i 
    p = len(str(i))
    total = 0
    while x>0 :
        rem = x%10
        total = total+rem**p
        x = x//10
    if i == total:
        print(i)
