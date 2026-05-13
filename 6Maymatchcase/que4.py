'''
4. Electricity Bill Management System

You are developing an Electricity Bill Management System for a power distribution company. The system helps calculate electricity bills for customers based on their unit consumption.

Sometimes, the operator may try to calculate the bill or apply surcharge before entering the number of units consumed. Your system must handle such situations properly.

👉 Important Condition:
If units are not entered, the system should display:
"Please enter units consumed first"
and should not perform further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Units Consumed
2 → Calculate Bill Amount

* First 100 units → ₹5 per unit
* Next 100 units → ₹7 per unit
* Above 200 units → ₹10 per unit
  3 → Apply Surcharge
* If bill > 2000 → 10% surcharge
* Otherwise → 5% surcharge
  4 → Display Final Bill
  5 → Exit

---

Sample Run 1:
Input:
Enter your choice: 2

Output:
Please enter units consumed first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter units consumed: 250

Output:
Units recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
Bill Amount: 1700

(Explanation: 100×5 = 500, 100×7 = 700, 50×10 = 500 → Total = 1700)

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Surcharge: 85

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
----- Final Bill -----
Units: 250
Bill Amount: 1700
Surcharge: 85
Total Payable: 1785

---

Sample Run 6 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 7 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!
'''







unit = 0 
bill=sub=0
while True:
    print("Menu Options:\n1 → Enter Units Consumed\n2 → Calculate Bill Amount\n3 → Apply Surcharge\n4 → Display Final Bill\n5 → Exit")
    ch = int(input("Enter the choice : "))
    
    
    match ch:
        case 1 :
            s = int(input("Enter units consumed: "))
            print("Units recorded successfully")
            unit = s
        case 2 :
            if unit == 0:
                 print("Please enter units consumed first")
            else:
                bill = unit*5 if unit<=100 else (100*5+(unit-100)*7) if unit>100 and unit<=200 else (100*5)+(100*7)+(unit-200)*10
                print("Bill Amount:", bill)
        case 3 :
            if unit == 0:
                 print("Please enter units consumed first")
            else:
                sub = (bill//100)*10 if bill>2000 else (bill//100)*5 
                print(f"Surcharge: {sub}")
        case 4 :
            if unit == 0:
                 print("Please enter units consumed first")
            else:
                print(f"----- Final Bill -----\nUnits: {unit}\nBill Amount: {bill}\nSurcharge: {sub}\nTotal Payable: {bill+sub}")
        case 5 :
            print("Exiting system... Thank you!")
            break
        case _:
            print("Invalid choice. Please try again.")