# WAP to check the no. is even or odd without modules operator

'''
Logic :- 
1 - 0001
4 - 0100
---------
0 - 0000
---------

1 - 0001
3 - 0011
--------
1 - 0001
'''

n = int(input("Enter the number : "))

if n&1 == 0:
    print("Even")
else:
    print("Odd")


#WAP to swap two without using 3variable

a = 10 
b = 20
a = a^b
b = a^b
a = a^b

print(a)
print(b)









