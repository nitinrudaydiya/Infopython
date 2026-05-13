***# FOR ELSE***



In python for can have an optional else block in other programming languages the use of else is only with if but python allow else condition with loops.

The else block after for loop is executed on when the loop is not terminated by a break statement. If the loop is terminate by break else block is skip.





SYNTAX : for variable in sequence:

            loop body

            if condition:

               break



         else:

             print("statements for no break")







**Advantage :**

            Cleaner code for searching problems - State of using a saperate flag variable to check condition was met or not FOR ELSE can be use .

            Logical Clearity

            Useful in prime number checking

***// Practice question***

***# FOR ELSE***

***'''***



for i in range (1,10):

    print(i)

else:

    print("No break")





for i in range (1,10):

    print(i)

    if i == 20:

        break             # break chal to else nahi chalega

else:

    print("No break")     #else tab hi chalega jab break nahi chalega









for i in range (1,10):

    print(i)

    if i == 5 :

        break

else:

    print("No break")    #Else nahi chalega kyuki break chalega











\#PRIME NUMBER USING FOR ELSE



n = int(input("Enter the number : "))



if n <= 1:

    print("Not prime")

else:

    for i in range(2,n):

        if n%i == 0:

            print("Not prime")

            break

    else:

        print("Prime")

'''

'''



\#FIND NUMBER IN LIST USING FOR ELSE:



num = \[1,2,4,6,8,10]

target = 11

for i in num :

    if i == target :

        print("Banda mil/ gaya")

        break

else:

    print("Banda nahi(X) mila")

