'''
Assignment 2: Salary Calculator

Write a Python program that:

Accepts daily wage and number of days.
Calculates total salary.

Input:
Daily wage = 500
Days = 26

Output:
Salary = 13000
----------------------------------------------
'''

wage = int(input("Daily wage : "))
days = int(input("Days : "))
Salary = wage*days
print(f"Salary = {Salary}")

