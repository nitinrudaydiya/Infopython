'''

29) Diagonal Number Square
    1 - - -
    - 2 - -
    - - 3 -
    - - - 4

'''
n = int(input("Enter the rows : "))

i = 1

while i<=n-1:
    print()
    j = 1
    while j < n :
        if i==j :
            print(j,end=" ")
        else :
            print("-",end=" ")
        j+=1
    i+=1