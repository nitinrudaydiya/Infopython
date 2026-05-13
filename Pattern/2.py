'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 

'''
'''
n = int(input("Enter the number : "))
i = n
while i>=1:
    print()
    j = i
    while j>=1: 
       print(j,end=" ")
       j = j-1
    i=i-1
'''
n = int(input("Enter the number : "))
for i in range(n,0,-1):
    print()
    for j in range(i,0,-1):
        print(j,end=" ")
