'''
1. Utility Toolkit System

You are developing a Utility Toolkit Application for a small office. Employees use this tool to quickly perform common number operations like checking prime numbers, reversing numbers, etc.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Check Prime Number
2 → Check Palindrome Number
3 → Reverse a Number
4 → Count Digits
5 → Exit

Sample Run 1:
Input:
Enter your choice: 1
Enter number: 7

Output:
7 is a Prime Number

Sample Run 2:
Input:
Enter your choice: 2
Enter number: 121

Output:
121 is a Palindrome Number

Sample Run 3:
Input:
Enter your choice: 3
Enter number: 456

Output:
Reversed Number is: 654

Sample Run 4:
Input:
Enter your choice: 4
Enter number: 98765

Output:
Total digits: 5

Sample Run 5 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

Sample Run 6 (Exit):
Input:
Enter your choice: 5

Output:
Exiting program... Thank you!

Requirements:

* Use while loop to repeat menu
* Use match-case for decision making
* Handle negative numbers properly
* Use only loops and conditions
'''
while True:
    print("Menu Options:\n1 → Check Prime Number\n2 → Check Palindrome Number\n3 → Reverse a Number\n4 → Count Digits\n5 → Exit")
    ch = int(input("Enter the choice : "))
    match ch:
        case 1:
            n = int(input("Enter the number : "))
            if n<=1:
                print(n,"is not a Prime number")
            else:
                for i in range(2,int(n**0.5)+1):
                    if n%i==0 :
                       break
                else:
                    print(n,"is a prime number")
        case 2 :
            n = int(input("Enter the number : "))
            org = n
            rev = 0
            while n>0 :
                rem = n%10
                rev = rev*10+rem
                n //= 10
            if org == rev :
                print(org,"is a Palindrome Number")
            else:
                print(org,"and",rev,"are not a Palindrome Number")
        case 3 :
            n = int(input("Enter the number : "))
            org = n
            rev = 0
            while n>0 :
                rem = n%10
                rev = rev*10+rem
                n //= 10
            print("Reversed Number is:",rev)
        case 4:
            n = int(input("Enter the number : "))
            count = 0
            while n>0 :
                rem = n%10
                count += 1
                n //= 10
            if count==0:
                print("Total digits:",1)
            else:
                print("Total digits:",count)
        case 5:
              print("Exiting program... Thank you!")
              break
        case _:
              print("Invalid choice. Please try again.")
  


                 
