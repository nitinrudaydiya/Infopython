#WAP 
n = int(input("Enter first number : "))
m = int(input("Enter second number : "))

for i in range(n,m+1):
    for j in range(1,11) :
        print(f"{i} x {j} = {i*j}",end=" ")
        print()
    print()