'''
Assignment 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500
'''

Distance = int(input("Distance = "))
Mileage = int(input("Mileage = "))
price = int(input("Petrol Price = "))

cost = (price//Mileage)*Distance
print(f"Cost = {cost}")