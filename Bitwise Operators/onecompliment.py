'''
#one's complement (Bitwise not): one's complement (Bitwise not) all one's will be converted into 0 and all 1 will be converted 1 .
     It perform Bitwise negation .
'''

a = 4        #0000 0000 0000 0100

print(~a)    #1111 1111 1111 1011


'''
# SHORTCUT :- a = 4 and one's complement - 4+1 -> 5  convert into negative -5
# 2nd method :- 0000 0000 0000 0100 
                                 +1
                0000 0000 0000 0101  -> 5 -> convert into negative -5


         Ex. :- a = 7
                0000 0000 0000 0111
                                 +1
                0000 0000 0000 1000  -> 8 -> convert into negative -8
# 3rd method :-   a = 5 
       binary no. ->  0000 0000 0000 0101
   convert one's  ->  1111 1111 1111 1010
      compliment      1= (-)
                  ->  -1-2^3-2^0 = -6ans
# 13 -> 0000 0000 0000 1101
one's-> 1111 1111 1111 0010
two's-> 0000 0000 0000 1101
                         +1
        0000 0000 0000 1110
        -14

#  -1 -> 1111 1111 1111 1111
   -9 -> 1111 1111 1111 0111
        0000 0000 0000 1000
        -> 8        


'''