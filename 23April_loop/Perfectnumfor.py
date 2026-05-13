# Using for loop Perfect num \

n1 = int(input("Enter the number : "))
i = 1
sum = 0

for i in range(1,n1):
    if n1%i == 0 :
        sum = sum+i

if n1 == sum:
    print(n1, "is a Perfect number")
else:
    print(n1, "is not a Perfect number")


