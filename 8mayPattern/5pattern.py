'''
5)
A
AB
ABC
ABCD
ABCDE
'''

n = int(input("Enter the number : "))
i = 1

while i<=n:
    print()
    j = 1
    ch = 65 
    while j<=i:
        print(chr(ch),end="")
        ch+=1 
        j+=1
    i = i+1





for i in range(1,n+1):
    print()
    ch = 65
    for j in range(1,i+1):
        print(chr(ch),end="")
        ch+=1