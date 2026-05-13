n = int(input("Enter first number : "))
m = int(input("Enter second number : "))


for i in range(n,m+1):
    temp = i
    p = len(str(i))
    total = 0 
    while temp > 0 :
        digit = temp%10
        total = total+digit**p
        temp//=10
    if total == i:
        print(i)