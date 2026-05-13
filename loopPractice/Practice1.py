'''s  = input("Enter the string : ")

for i in s:
   if i in "aeiouAEIOU":
        continue
   print(i ,end = "")
'''
'''
a = input("Enter the string : ")

for j in a :
    if j=="a" or j=="e" or j=="i" or j=="o" or j=="u":
        continue
    print(j , end="")

#WAP to skip even no. stop at 9 do nothing for 5:

for i in range(1,11):
     if i%2==0:
        continue
     elif i == 9 :
        break
     elif i == 5 :
        pass 
     else:
        print(i)
     
  '''    


# FOR ELSE
'''

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





#PRIME NUMBER USING FOR ELSE

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

#FIND NUMBER IN LIST USING FOR ELSE:

num = [1,2,4,6,8,10]
target = 11
for i in num :
    if i == target :
        print("Banda mil/ gaya")
        break
else:
    print("Banda nahi(X) mila")




'''


#  WHILE ELSE


attempt = 0

while attempt<3:
    password = input("Enter the password: ")
    if password == "admin":
        print("Granted")
        break
    
    attempt+=1
else:
    print("TOO many attempt")
    










