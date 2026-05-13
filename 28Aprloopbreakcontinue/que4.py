'''
4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31
'''

n = int(input())

if n <= 1:
    print("Not Prime")

else:
    count = 0
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            break
    
    if count == 0:
        print("Prime Number")
        
        num = n
        while True:
            num += 1
            c = 0
            
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    c += 1
                    break
            
            if c == 0:
                print("Next Prime =", num)
                break
    
    else:
        print("Not Prime")
        
        num = n
        while True:
            num -= 1
            
            if num <= 1:
                break
            
            c = 0
            
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    c += 1
                    break
            
            if c == 0:
                print("Previous Prime =", num)
                break