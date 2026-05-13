'''
5.
Strong Number Detector

A banking security system uses Strong Numbers for special authentication testing.
The user enters a range of numbers.
The system identifies all Strong Numbers between the given range using nested loops.

A Strong Number is a number in which the sum of factorials of its digits is equal to the original number.

Example:
145

1! + 4! + 5!
= 1 + 24 + 120
= 145

Since the sum is equal to the original number, 145 is called a Strong Number.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Strong Numbers are:
1
2
145
'''

n = int(input("Enter the number : "))
m = int(input("Enter the number : "))
x = n
i = 1
while n<m :
    while x<0 :
        rem = x%10
        i *= rem
        x //= 10
    print(i)
    n+=1
    
    