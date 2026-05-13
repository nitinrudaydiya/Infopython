'''
    1
   12
  123
 1234
12345
'''


n = int(input("Enter the row : "))

i = 1 

while i<=n:
    print()
    s = 1
    while s<=n-i:
        print(" ",end= "")
        s+=1
    j = 1
    while j<=i:
        print(j,end="")
        j=j+1
    i+=1


