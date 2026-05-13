'''
30) Extended Slanted Star Block
    ****
     ****
      ****
       ****
        ****
'''
n = int(input("Enter the row : "))

for i in range(n,0,-1):
    print()
    for j in range(n,i-1,-1):
        print(" ",end="") 
    for k in range(n-1,0,-1):
        print("*",end="")