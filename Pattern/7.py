'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15 


'''
n = int(input("Enter the number : "))
i = 1
k=1

while i<=n:
    print()
    j = 1
    while j<=i :
         print(k,end=" ")
         j=j+1
         k=k+1
    i=i+1
l=1
for i in range(1,n+1):
    print()
    for j in range(1,i+1):
        print(l,end = " ")
        l=l+1