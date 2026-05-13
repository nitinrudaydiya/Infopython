'''

Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5
'''

sal = int(input("Monthly salary = "))
day = int(input("Working days = "))
hour = int(input("Working hours per day = "))

day_sal = sal/day
hour_sal = day_sal/hour

print(f"Salary per day = {day_sal}\nSalary per hour = {hour_sal}")

