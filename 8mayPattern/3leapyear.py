'''
3)	WAP to find out all the leap years between two entered years
'''

n = int(input("Enter the Start number : "))
m = int(input("Enter the End number : "))
i = n
while i<=m:
    if (i%4==0 and i%100!=0 ) or i%400==0 :
        print(i,"is leap year")
    i=i+1


for i in range(n,m+1):
    if (i%4==0 and i%100!=0 ) or i%400==0 :
        print(i,"is leap year")

    