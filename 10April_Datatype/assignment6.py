'''
========================================
Assignment 6: Smart Coin Machine
========================================

You insert an amount into a vending machine. It returns coins using the largest denominations possible (₹10 and ₹5).

Write a Python program that:
- Accepts the total amount.
- Calculates how many ₹10 coins and ₹5 coins will be dispensed.
- Displays the result.

Example:
Amount = ₹35
Output = ₹10 x 3, ₹5 x 1
'''

Total = int(input("Enter total amount : "))
tencoin = Total//10
fivecoin = (Total%10)//5
print(f"Amount = ₹{Total}\nOutput = ₹10 x {tencoin}, ₹5 x {fivecoin}")