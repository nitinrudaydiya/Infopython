#PYTHON MATCH CASE STATEMENT 
'''
It is introduce in python3.10
It allow as to perform more readable checks
It is use to create menu driven program

SYNTAX : match variable :
             case pattern1:
                 code block1
             case pattern2:
                 code block2
         -----------------------
         -----------------------
             case _:
                  default block
'''


a = int(input("Enter choice : "))
match a:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Wrong choice")