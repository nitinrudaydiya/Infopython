# WAP to print perfect Number 

'''
n = int(input("Enter the number : "))
sum = 0
for i in range(1,n):
    if n%i == 0 :

        sum += i


print("Perfect Number:",sum)

'''

#Using While loop 

n1 = int(input("Enter the number : "))
i = 1
sum = 0

while i>n:
    if n1%i == 0 :
        sum = sum+i
    i = i+1

if n == sum:
    print(n1, "is a Perfect number")
else:
    print(n1, "is not a Perfect number")




n1 = int(input("Enter the number : "))
i = 1
sum = 0

while i>=n//2:
    if n1%i == 0 :
        sum = sum+i
    i = i+1

if n == sum:
    print(n1, "is a Perfect number")
else:
    print(n1, "is not a Perfect number")


