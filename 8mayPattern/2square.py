'''2)	WAP to print Square, Cube and Square Root of all numbers from 1 to N
'''


n = int(input("Enter the number : "))
i = 1
while i<=n:
    print(f"Square of {i} = {i**2}")
    print(f"Cube of {i} = {i**3}")
    print(f"Square Root of {i} = {i**0.5}")
    i+=1

for i in range(1,n+1):
    print(f"Square of {i} = {i**2}")
    print(f"Cube of {i} = {i**3}")
    print(f"Square Root of {i} = {i**0.5}")
