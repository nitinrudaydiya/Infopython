'''
a = int(input("Enter the choice 1 : "))

match a :
    case 3:
        print("Three")
    case 1:
        print("One")
    case _:
        print("Wrong")   #Default code is not campasary 


print("Out of match case")



n = int(input("Enter the choice 2: "))


match n :
    case 3:
        print("Three")
    case 3:
        print("One")     #we give multiplesame conditions in python but not in another langauge
    case _:
        print("Wrong")   #Default code is not campasary 


print("Out of match case")


m = int(input("Enter the choice 3: "))


match m :
    case 3:
        print("Three")
    case 1|2|4:
        print("One")
    case _:
        print("Wrong")   #Default code is not campasary 


print("Out of match case")






n = int(input("Enter the choice : "))


match n%2 :
    case 0:            #pass expression in the match case
        print("Even")
    case 1:
        print("Odd")
    case _:
        print("Wrong") 

print("Out of match case")


day = input("Enter the day : ").lower()


match day :
    case "monday":
        print("Start")
    case "sunday":
        print("Rest")
    case _:
        print("Working day") 

print("Out of match case")



a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
op = input("Enter the Operator(+,-,/,*) : ")

match op :
    case "+":
        print("Sum = ", a+b)
    case "-":
        print("Substraction = ", a-b)
    case "*":
        print("Multiplication = ", a*b)
    case "/":
        if b!=0 :
            print("Sum = ", a/b)
        else : 
            print("Infinite")
    case _:
        print("Wrong") 

print("Out of match case")
'''

day = input("Enter the Vowel or consonent : ").lower()


match day :
    case "a"|"e"|"i"|"o"|"u":
        print("Vowel")
    case "`"|"@"|"#"|"%"|"!":
        print("Special Charecter")
    case _:
        print("Consonent	") 

print("Out of match case")