'''
Assignment 14: Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0

'''

CP = int(input("Cost Price = "))
SP = int(input("Selling Price = "))
profit = SP-CP
profitperc = (profit/CP)*100
print(f"Profit = {profit}\nProfit % = {profitperc}")