'''
8.
enter n6
 654321
  65432
   6543
    654
     65
'''
n = int(input("Enter the rows : "))
i = 1
while i<=n-1:
    print()
    j=1
    while j<=i:
        print(" ",end="")
        j+=1
    k=n
    while k>=i:
        print(k,end="")
        k-=1
    
     
    i+=1


for i in range(1,n):
    print()
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(n,i-1,-1):
        print(k,end="")