'''========================================
Assignment 3: Split the Bill
========================================

You and your friends went out to eat. The bill was quite high and you want to split it evenly.

Write a Python program that:
- Accepts the total bill amount.
- Accepts the number of friends.
- Displays how much each person should pay.

Example:
Total bill = 1250
Friends = 5
Each should pay = 250.0'''


total_bill = int(input("Enter the bill Amount: "))
friends = int(input("Enter number of friends: "))
print(f"Total bill is {total_bill} and Number of friend is {friends} each person should pay{total_bill/friends}")




