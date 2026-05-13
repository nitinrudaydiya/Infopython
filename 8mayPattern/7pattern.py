'''7.
enter n6
     *
    **
   ***
  ****
 *****
******
'''


n = int(input("Enter the rows: "))

i = 1

while i<=n:
    print()
    j=n-1
    while j>=i:
        print(" ",end="")
        j-=1
    k=1
    while k<=i:
        print("*",end="")
        k+=1
    i+=1



for i in range(1,n+1):
    print()
    for j in range(n-1,i-1,-1):
        print(" " ,end="")
    for k in range(1,i+1):
        print("*",end="")