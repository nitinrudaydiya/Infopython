''
n = int(input("Enter the Num : "))
sum =  0
while n > 0 :
    rem = n%10
    sum = sum + rem
    n //= n

print(f"sum of digits is {sum}")'''