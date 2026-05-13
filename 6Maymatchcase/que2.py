'''
2.
 Employee Salary Processor

Scenario:
You are developing an Employee Salary Processing System for a company’s HR department. The system is used to manage and calculate employee salary details such as allowances, tax deductions, and final payable salary.

The HR staff may not always follow the correct sequence while using the system. For example, they might try to calculate net salary or tax before entering the basic salary. Your program must handle such situations properly.

👉 Important Condition:
If the Basic Salary is not entered, the system should display:
"Please enter basic salary first"
and should not perform any further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Basic Salary
2 → Calculate HRA (20%) and DA (10%)
3 → Calculate Net Salary
4 → Tax Deduction

* Salary > 50000 → 10% tax
* Otherwise → 5% tax
  5 → Display Salary Slip
  6 → Exit

---

Sample Run 1:
Input:
Enter your choice: 3

Output:
Please enter basic salary first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter Basic Salary: 40000

Output:
Basic Salary recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
HRA: 8000
DA: 4000

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Net Salary (before tax): 52000

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Tax Deduction: 5200

---

Sample Run 6:
Input:
Enter your choice: 5

Output:
----- Salary Slip -----
Basic Salary: 40000
HRA: 8000
DA: 4000
Net Salary: 52000
Tax: 5200
Final Salary: 46800

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 6

Output:
Exiting program... Thank you!
'''
salary = 0
while True:
    print("Menu Options:\n1 → Enter Basic Salary\n2 → Calculate HRA (20%) and DA (10%)\n3 → Calculate Net Salary\n4 → Tax Deduction\n5 → Display Salary Slip\n6 → Exit")
    ch = int(input("Enter the choice : "))
    
    
    match ch:
        case 1 :
            s = int(input("Enter the Basic Salary : "))
            print("Basic Salary recorded successfully")
            salary = s
        case 2 :
            if salary == 0 :
                print("Please enter basic salary first")
            else:
                HRA = (salary//100)*20 
                DA = (salary//100)*10        
                print(F"HRA: {HRA}\n DA: {DA}")
        case 3 :
            if salary == 0 :
                print("Please enter basic salary first")
            else:
                Net = salary+(salary//100)*20+(salary//100)*10
                print("Net Salary (before tax):",Net)
        case 4 :
            if salary == 0 :
                print("Please enter basic salary first")
            else:
                x = ((salary+(salary//100)*20+(salary//100)*10)//100)*10 if (salary+(salary//100)*20+(salary//100)*10) > 50000 else ((salary+(salary//100)*20+(salary//100)*10)//100)*5
                print("Tax Deduction:",x)
        case 5 :
            if salary == 0 :
                print("Please enter basic Details first")
            else:
                print(f"----- Salary Slip -----\nBasic Salary: {salary}\nHRA: {(salary//100)*20}\nDA: {(salary//100)*10}\nNet Salary: {salary+(salary//100)*20+(salary//100)*10}\nTax: {((salary+(salary//100)*20+(salary//100)*10)//100)*10 if (salary+(salary//100)*20+(salary//100)*10) > 50000 else ((salary+(salary//100)*20+(salary//100)*10)//100)*5}\nFinal Salary: {(salary+(salary//100)*20+(salary//100)*10)-((salary+(salary//100)*20+(salary//100)*10)//100)*10 if (salary+(salary//100)*20+(salary//100)*10) > 50000 else ((salary+(salary//100)*20+(salary//100)*10)//100)*5}")
        case 6 :
            print("Exiting program... Thank you!")
            break


      
         