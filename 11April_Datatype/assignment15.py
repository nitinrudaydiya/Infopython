'''
Assignment 15: Average Speed for Multiple Trips

Write a Python program that:

Accepts distance1, time1, distance2, time2.
Calculates average speed.

Input:
Distance1 = 60
Time1 = 1
Distance2 = 40
Time2 = 1

Output:
Average Speed = 50 km/h
'''



distance1 = int(input("Distance1 = "))
time1 = int(input("Time1 = "))
distance2 = int(input("Distance2 = "))
time2 = int(input("Time2 = "))

speed1 = distance1//time1
speed2 = distance2//time2
avg_speed = (speed1+speed2)//2
print(f"Average Speed = {avg_speed} km/h")