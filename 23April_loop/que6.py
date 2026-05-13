'''
6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to **check whether a number is an Armstrong number using loops**.

Input: 153
Output: Armstrong
'''
'''

num = int(input("Enter the number = "))
num1 = num
Armstrong = 0 

while num > 0 :
    rem = num%10
    Armstrong += rem**3
    num //= 10

if num1 == Armstrong:
    print("Armstrong")
else:
    print("Not Armstrong")



#Using for loop

num2 = int(input("Enter the num : "))
temp = num2
string = ""

for j in str(num2):
    rem = (int(num2))%10
    string +=str(rem**3)
    num2 = str(int(num2)//10)
if temp == Armstrong:
    print("Armstrong")
else:
    print("Not Armstrong")


'''

#REAL USE 
num3 = int(input("Enter the num : "))#153
temp1 = num3
e = len(str(temp1))#3

string = 0

for j in str(num3):
    rem = (int(num3))%10
    string +=int(rem**e)
    num3 = str(int(num3)//10)
if temp1 == string:
    print("Armstrong")
else:
    print("Not Armstrong")


