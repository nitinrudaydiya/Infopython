'''
Assignment 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0
'''

dis = int(input("Distance = "))
mileage = int(input("Mileage = " ))
PP = int(input("Per litre Petrol price = "))

PU = dis/mileage
cost = PU*PP
print(f"Petrol Used = {PU} litres\nTotal Cost = {cost}")