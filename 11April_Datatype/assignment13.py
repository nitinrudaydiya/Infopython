'''
Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0
'''

principal = int(input("Principal = "))
rate = int(input("Rate = "))
time = int(input("Time = "))

ci = round((principal*((1 + rate/100)**time)-principal),2)
amount = ci + principal

print(f"Amount = {amount} \nCompound Interest = {ci}") 