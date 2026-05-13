'''WAP to print prime numbers between 2 numbers:-
n = int(input("Enter first number : "))
m = int(input("Enter second number : "))


while n<=m:
    x=n
    flag=True
    if x > 1:
       i = 2
       while i < x :
          if x%i==0:
              flag=False
              break
          i+=1
       if flag==True :
          print(x)
       
    n+=1
'''

n = int(input("Enter first number : "))
m = int(input("Enter second number : "))


while n<=m:
    x=n
    if x > 1:
       i = 2
       while i < x :
          if x%i==0:
              break
          i+=1
       else:
           print(x)
    n+=1