''' 
1 * * * * * * * * * * 1
1 2 * * * * * * * * 2 1
1 2 3 * * * * * * 3 2 1 
1 2 3 4 * * * * 4 3 2 1 
1 2 3 4 5 * * 5 4 3 2 1
1 2 3 4 5 6 6 5 4 3 2 1 

'''

n = int(input("Enter the row : "))

i = 1 

while i<=n:
     print()
     j=1
     while j<=i:
        print(j,end= " ")
        j+=1

     s=1
     while s<=(n-i)*2:
        print("*",end=" ")
        s=s+1

     k = i
     while k>=1:
        print(k,end = " ")
        k-=1
     i=i+1

'''
n = int(input("Enter the row : "))

i = 1 
for i in range(1,n+1):
    print()
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range((n-1)*2,1,-1):
        print("*",end=" ")
    for l in range(i,0,-1):
        print(l,end=" ")
'''