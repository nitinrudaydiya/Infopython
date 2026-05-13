'''

5) Number-Star Palindrome
    12344321
    123**321
    12****21
    1******1
'''

n = int(input("Enter the row : "))

i = 1
while i<=n:
    print()
    j=1
    while j<=n:
        print(j,end="")
        j+=1
    i+=1

