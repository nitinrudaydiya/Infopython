'''
10.
enter number6
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4

'''

n= int(input("Enter the rows : "))
i = 1

while i<=n:
    print()
    j=0
    while j<=i-2:
        print(j,end=" ")
        j+=1
    i+=1


for i in range(1,n+1):
    print()
    for j in range(0,i-1):
        print(j,end=" ")