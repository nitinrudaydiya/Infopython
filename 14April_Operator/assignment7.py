'''
Assignment 7: Cricket Run Rate
In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67
'''

runs = int(input("Total runs = "))
overs,balls = map(int,input("Overs and balls = ").split("."))
balls = overs*6+balls
overs1 = balls/6
RR = round(runs/overs1,2)
print(f"Total Balls = {balls}\nRun Rate = {RR}")