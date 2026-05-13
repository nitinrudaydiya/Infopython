'''
#Bite wise operator

Python bite wise operator are use to perform bite wise calculation on interger
The integer are first converted into binary than operation are perform on each 
The Result is returns in Decimal formate


#list of bite wise operator

& Bitewise AND 
| OR
^ XOR
<<  left shift 
>> right shift
- one's complement (Bitewise not)

a  b  a&b  a|b  a^b
0  0   0    0    0 
0  1   0    1    1
1  0   0    1    1 
1  1   1    1    0

'''

a = 5
b = 6 

print(a&b)
print(a|b)
print(a^b)
