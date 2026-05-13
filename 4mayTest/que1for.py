num = input()

c0=c1=c2=c3=c4=c5=c6=c7=c8=c9=0
i = 0

while i < len(num):
    ch = num[i]
    if ch=='0': 
        c0+=1
    elif ch=='1': 
        c1+=1
    elif ch=='2': 
        c2+=1
    elif ch=='3': 
        c3+=1
    elif ch=='4': 
        c4+=1
    elif ch=='5': 
        c5+=1
    elif ch=='6': 
        c6+=1
    elif ch=='7': 
        c7+=1
    elif ch=='8': 
        c8+=1
    elif ch=='9': 
        c9+=1
    i += 1

print("Repeated Digits:", end=" ")
total=0
found=0

if c0>1: 
    print(0,end=" ")
    total+=c0
    found=1
if c1>1: 
    print(1,end=" ")
    total+=c1
    found=1
if c2>1: 
    print(2,end=" ")
    total+=c2
    found=1
if c3>1: 
    print(3,end=" ")
    total+=c3
    found=1
if c4>1: 
    print(4,end=" ")
    total+=c4
    found=1
if c5>1: 
    print(5,end=" ")
    total+=c5
    found=1
if c6>1: 
    print(6,end=" ")
    total+=c6
    found=1
if c7>1: 
    print(7,end=" ")
    total+=c7
    found=1
if c8>1: 
    print(8,end=" ")
    total+=c8
    found=1
if c9>1: 
    print(9,end=" ")
    total+=c9
    found=1

if found<0:
    print("\nUnique Number")
else:
    print("\nTotal Repeated Count =", total)
    if c0>m:
        m,d = c0,0
    if c1>m: 
        m,d=c1,1
    if c2>m: 
        m,d=c2,2
    if c3>m: 
        m,d=c3,3
    if c4>m:
        m,d=c4,4
    if c5>m:
        m,d=c5,5
    if c6>m: 
        m,d=c6,6
    if c7>m:
        m,d=c7,7
    if c8>m: 
        m,d=c8,8
    if c9>m:
        m,d=c9,9

    print("Max Frequency Digit =", d)
    print("Repeated Pattern Detected")


