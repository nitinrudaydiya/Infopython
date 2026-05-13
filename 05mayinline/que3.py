'''
3. Employee Bonus Distribution System
A company provides bonuses based on years of experience.
Experience >10 years → 30% bonus
Experience >5 years → 20% bonus
Otherwise → 10% bonus
Write a program to calculate the total salary after adding bonus using inline if.
'''

exp = int(input("Enter the experience in Year : "))
sal = int(input("Enter the current salary : "))
bonus = (sal//100)*30 if exp>10 else (sal//100)*20 if exp>5 else (sal//100)*10

total = sal+bonus

print("Total salary after adding bonus =", total)