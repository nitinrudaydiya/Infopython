'''
#Identity Operator : THE identity operator are used to compare the object if both objects are same datatypes and shares same memory location 

there are difference identity operator available 

is Operator : the is operator checks if 2 variable point to the same object (Same memory location)
2. is not Operator : It is opposite of is if to valiable point to difference object than its returns True otherwise returns False 
'''

a = 10
b = 10

print(a is b)   #True
print(a is not b) #False

a = [10,20]
b = [10,20]

print(a is b)#False
print(a == b)#True


the Equality operator is use to compare the value of two where is identity operator used to compare location.

a = "Nitin"
n = "Nitin"
print(a is b)#True
print(a == b)#True
