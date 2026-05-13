'''
1 
2 2
3 3 3 
4 4 4 4
5 5 5 5 5 




'''
n = int(input("Enter the number : "))
i = 1

while i <= n :
    print()
    j=1
    while j<=i:
        print(i,end = " ")
        j = j+1
    i = i + 1


for i in range(n,0,-1):
    print()
    for j in range(i,0,-1):
        print(i,end = " ")
