#ARMSTOM NUM USING WHILE LOOP 

num = int(input("Enter number : "))
temp = num 
arm = 0
l = len(str(num))


while num > 0 :
    rem = num%10
    arm = arm + rem**l
    num //= 10

if arm == temp:
    print("Armstrong number ")
else:
    print("Not Armstrong")
    
    