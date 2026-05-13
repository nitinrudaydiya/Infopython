'''

2. Multi Stage Prime Lock System

A smart locker opens only if final derived number is prime.

Write a program to:

- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not

Input:
234

Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime

'''

n = input("Enter the number : ")
sum =  0
pro = 1 
for i in n :
    j = int(i)
    sum += j
    pro *= j
    
dif = abs(pro - sum)
dig = len(str(dif))
final = dig + dif

print("Sum =",sum)
print("Product =",pro)
print("Difference =",dif)
print("Digits =",dig)
print("Final Result =",final)


if final <=1 :
    print("Not Prime")
else :
    for i in range(2,int(final**0.5)+1):
        if final % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
    