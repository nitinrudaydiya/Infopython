'''
Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750
'''
hour = int(input("Hours = "))
minutes = int(input("Minutes = "))
Seconds = int(input("Seconds = "))

sec = (hour*3600)+(minutes*60)+Seconds

print(f"Total Seconds = {sec}")