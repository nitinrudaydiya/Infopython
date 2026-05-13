'''
Conditional Expression(Ternary Operator) :- 1. It is also called in line if it allow Writing if else in a single line.
                                            2. The ternary operator in python perform conditional check and assign values or execute expression in a single line.


SYNTAX :- x = value1 if condition else value2 

if condition is True than it return value1 
if condition is False than it return value2


ADVANTAGE OF 
1. Concisis : It reduce multiple line to one line 
2. Readable : It imidiatly shows condition and result Suppose in line decision not need to break code into multiple lines
'''
'''
s = 30 if 10<20 else 40
print(s) # agar if true hai to 30 print hoga nahi hai true to 40 print hoga


n = int(input("Enter the number : "))
if n%2 == 0 :
   print("Even")
else:
   print("Odd")

#Using Ternary
n = int(input("Enter the number : "))
x = "Even" if n%2 == 0 else "Odd"
print(x) 

# Find max in two Number

a = int(input("Enter the number 1 : "))
b = int(input("Enter the number 2 : "))
max = a if a>b else b 
print(max)

# Second way 
print(a,"is greater than",b) if a>b else print(b,"is greater than",a)


x = 10 if 20<30 else 40 if 50<60 else 70
print(x)

y = 10 if 200<30 else 40 if 50<60 else 70
print(y)

z = 10 if 200<30 else 40 if 500<60 else 70
print(z)

#Greater in 3 numbers

a = int(input("Enter the number 1 : "))
b = int(input("Enter the number 2 : "))
c = int(input("Enter the number 3 : "))

max = a if a>b and a>c else b if b>c else c 
print(max,"is greater")


a = int(input("Enter the number 1 : "))
b = int(input("Enter the number 2 : "))
print("A is Equal to B" if a==b else "A is greater" if a>b else "A is small")



i = 1 
while i<=10:
    print(i,"Even") if i%2 ==0 else print(i,"Odd")
    i+=1 
'''

i = 1 
while i<=10:
    print(i,"Even" if i%2 ==0 else "Odd")
    i+=1 

