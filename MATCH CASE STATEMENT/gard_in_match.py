''' Gard's in Match case : A Gard is an additional condition return using if inside a case .
                          It allow you to Add extra checking logical to a case pattern.
                          A case execute only if the pattern matches and the Gard condition is TRUE.
'''
'''
age = int(input("Enter the age : "))

match age :
    case x if x<13:
        print("child")
    case x if x<20:
        print("Teen")
    case x if x<50:
        print("Adult")    


print("Out of match case")

n = int(input("Enter the Number : "))

match n :
    case x if x%2==0:
        print("Even")
    case x :
        print("Odd")
  


print("Out of match case")

'''

while True:
    print("-----------------MENU-------------------------")
    print("1. Add Two number")
    print("2. Check Even or odd")
    print("3. Find Square")
    print("4. Exit")
    choice = int(input("Enter the choice : "))
    match choice:
        case 1 :
            a = int(input("Enter the 1st number : "))
            b = int(input("Enter the 2nd number : "))
            print("Sum =", a+b)
        case 2 :
            a = int(input("Enter the number : "))
            if a%2==0:
                print("Even")
            else:
                print("Odd")
        case 3 :
            a = int(input("Enter the number : "))
            print("Square of =",a,"is",a**2)
        case 4 :
            print("Exxxxxiiiiiitttttttiiiiinnnnnnggggggggg")
            break
        case _ :
            print("Invalid Choice Fill Correct Choice")

