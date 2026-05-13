'''
---

Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0

---
'''

price = int(input("Mobile price = "))
Dp = int(input("Down payment = "))
IR = int(input("Interest rate = "))
month = int(input("Months = "))

RA = price - Dp
total = (RA//100)*IR+RA
emi = (total/month)

print(f"Remaining Amount = {RA}\nTotal with Interest = {total}\nMonthly EMI = {emi}")