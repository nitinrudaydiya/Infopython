'''
6. Banking Fraud Detection System

A bank monitors transactions based on amount, location, OTP verification, and account age.

If transaction amount is at least 10000, then check location. If international, then check OTP verification. If verified, allow; otherwise block. If location is domestic, then check if amount is at least 50000. If yes, check account age. If account age is at least 2 years, allow; otherwise flag. If amount is less than 50000, allow. If transaction amount is less than 10000, then check unusual activity. If yes, flag; otherwise allow.

Input:
Transaction Amount = 60000
Location = domestic
Account Age = 1

Output:
Transaction Status = Flagged

'''


amount = int(input("Trasaction Amount = "))
location = input("Location = ").lower()
age = int(input("Account Age ="))

if amount >= 10000:
    if location == 'international':
        otp = input("OTP = ")
        if otp == "1234":
            print("Transaction Status = Allow")
        else:
            print("Transaction Status = Block")
    else:
        if amount >= 50000:
            if age >= 2 :
                print("Transaction Status = Allow")
            else:   
                print("Transaction Status = Flagged")
        elif amount <= 50000 :
            print("Transaction Status = Allow")
        elif amount <= 10000 :
            print("Transaction Status = Flagged")
        else:
            print("Transaction Status = Allow")


