'''
9. Smart Loan Eligibility System

A bank approves loans based on salary, age, credit score, and EMI.

If salary is 40000 or above, then check age. If age is between 21 and 60, then check credit score. If credit score is 750 or above, then check EMI. If EMI is less than or equal to 40% of salary, approve at 8%; otherwise approve at 10%. If credit score is below 750, then check if it is at least 650. If yes, approve at 12%; otherwise reject.

If salary is below 40000, then check if salary is at least 25000 and credit score is at least 700. If yes, approve at 13%; otherwise reject.

Input:
Salary = 50000
Age = 30
Credit Score = 760
EMI = 18000

Output:
Loan Status = Approved at 8%
'''

Sal = int(input("Salary = "))
Age = int(input("Age  = "))
CS = int(input("Credit Score = "))
EMI = int(input("EMI = "))

salary= (Sal//100)*40

if Sal >= 40000 :
    if Age >= 21 and Age <= 60 :
        if CS >= 750 :
            if EMI  <= salary :
                print("Loan Status = Approved at 8%")
            else:
                print("Loan Status = Approved at 10%")
        else:
            if CS>=650:
                print("Loan Status = Approved at 12%")
else:
    if salary >= 25000 and CS >= 700 :
        print("Loan Status = Approved at 13%")
    else:
        print("Loan Status = Rejected")
