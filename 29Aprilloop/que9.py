'''
9.
 Bike Service Kilometer Checker

A bike needs service every 3000 km.

Write a program to:

- Read travelled kilometers
- Print every service checkpoint till entered km

Input:
10000

Output:
3000 6000 9000
'''

km = int(input("Enter travelled kilometers: "))

service = 3000

while service <= km:
    print(service, end=" ")
    service += 3000