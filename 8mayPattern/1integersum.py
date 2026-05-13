'''
1)	WAP to find out the sum of all integer between 100 and 200 which are divisible by 9
'''

n = int(input("Enter the Start number : "))
m = int(input("Enter the End number : "))
i = n
sum = 0
while i<=m:
    if i%9 == 0:
        sum+=i
    i+=1
print(sum)

sum1 = 0
for i in range(n,m+1):
    if i%9 == 0:
        sum1+=i
    i+=1
print(sum1)
