'''
Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4
'''

seconds = int(input("Total seconds = "))
hours = seconds//3600
min = (seconds%3600)//60
sec = (seconds%3600)%60
print(f"Hours = {hours}\nMinutes = {min}\nSeconds = {sec}")
