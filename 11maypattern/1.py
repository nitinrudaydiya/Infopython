'''
1) Hollow Pyramid
        *
       * *
      *   *
     *     *
    *********
'''

n = int(input("Enter number : "))
i = 1


while i<=n:
    print()
    j=n-1
    while j>=i:
        print(" ",end="")
        j-=1
    k=n-1
    while k>=i:
        if k==i:
            print("*",end="")
        k-=1 
    m=0
    while m<=n-1:
        print(" ",end="")
        m+=1
    l = n
    while l>=i:
        if l==n :
           print("*",end="")
        l-=1
    i=i+1
    

for i in range(1,n*2):
     print("*",end="")