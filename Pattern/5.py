'''
1
* *
1 2 3
* * * *
1 2 3 4 5

'''

n = int(input("Enter the number : "))
i = 1


while i<=n:
    print()
    j = 1
    while j<=i:
        if i%2==0:
            print("*",end= " ")
        else:
            print(j,end= " ")
        j+=1
    i+=1



for i in range(1,n+1):
    print()
    for j in range(1,i+1):
        if i%2==0:
            print("*",end= " ")
        else:
            print(j,end= " ")
