'''
Bitwise left sift operator towards for left side n number of bites need to be dropped and 
towards from right side empty places need to be fill with 0 .
'''
a = 5           # 5*2^1  x<<n -> x * 2^n
print(a<<1)

# input 000 0000 0000 0000 0000 0000 0000 0101
# output - 000 0000 0000 0000 0000 0000 0000 0101 - 0000 0000 0000 0000 0000 0000 0000 1010

a = 3 
print(a<<3)

# input 0000 0000 0000 0000 0000 0000 0000 0011
# output 0000 0000 0000 0000 0000 0000 0000 0011 -> 0000 0000 0000 0000 0000 0000 0001 1000

a = 19 
print(a<<3)
print(a<<1)