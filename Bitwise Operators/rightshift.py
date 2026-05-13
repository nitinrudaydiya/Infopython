# (>>) Bitwise right shift Operator : In right shift toward right side n no. of bite to be dropped toward left side empty places fill with zeros for negative numbers we need to fill with one.

a = 5          # 0000 0000 0000 0101  -> 
print(a>>1)    # 0000 0000 0000 0010

a = 11         # 0000 0000 0000 1011   11 // 2^n ( x//2^n)
print(a>>1)    # 0000 0000 0000 0101 ->


### Negative number

# find negative no. binary 
# 0000 0000 0000 0101  -> 5
  -1 = 1111 1111 1111 1111
        
      = 1111 1111 1111 1011
       
       =-1-2^2
       = -1-4
       = -5


# 1111 1111 1111 1011
# right shift by 1 -> 1111 1111 1111 1101  
a = -5    
print(a>>1)
