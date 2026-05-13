'''
1
1 2                              --- Check Number of line
1 2 3                            --- Check starting point here is 1
1 2 3 4                          --- Line ending and relations 
1 2 3 4 5                        --- Check order here is increasing order 
'''
'''
n = int(input("Enter the number : "))
i = 1
while i<=n:
    print()
    j = 1 
    while j<=i:
        print(j,end= " ")
        j=j+1
    i=i+1

'''

n = int(input("Enter the number : "))
for i in range(1,n+1):
    print()
    for j in range(1,i+1):
        print(j,end = " ")

