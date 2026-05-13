'''
1. Smart Shopping Mall Discount System
A shopping mall offers discounts based on customer type and purchase amount.
If the customer is premium, they get 20% discount when the amount is more than 5000, otherwise 10%.
If the customer is regular, they get 10% discount when the amount is more than 3000, otherwise 5%.
Write a program to calculate the final payable amount using inline if only.
'''

type = input("Enter the type-(premium/regular) : " ).lower()
amount= int(input("Enter the amount : "))

dis =(amount/100)*20 if type=="premium" and amount > 5000 else  (amount/100)*10  if amount<5000 else (amount/100)*10 if type == "regular" and amount > 3000 else (amount/100)*5

final = amount - dis

print(f"Discount = {dis}\nFinal = {final}")