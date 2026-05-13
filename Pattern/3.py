''' 
1 2 3 4 5 
2 3 4 5 
3 4 5 
4 5 
5 
'''
'''
n = int(input("Enter the num : "))
i = 1
while i<=n:
    print()
    j = i
    while j<=n:
        print(j,end = " ")
        j = j+1
    i=i+1 

'''

n = int(input("Enter the num : "))
for i in range(1,n+1):
    print()
    for j in range(i,n+1):
        print(j,end= " ")
