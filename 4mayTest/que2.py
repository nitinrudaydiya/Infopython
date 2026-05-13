'''
2.
Digit Threshold Break Analyzer

A monitoring system analyzes numeric IDs to detect high-value digits. 
The system keeps adding digits one by one, but stops processing as soon as the running sum exceeds a given threshold.

Write a program to:

Accept a number and a threshold value
Traverse digits from right to left
Keep adding digits to a running sum
Display each digit added
The moment sum exceeds the threshold, stop using break
Display:
- Digits processed
- Final sum
- Count of digits processed
If threshold is never exceeded, print Threshold Not Reached

Use loops and break wherever required.

Input:
57294
Threshold = 10

Output:
Digits Processed: 4 9
Sum = 13
Count = 2
Threshold Exceeded

Input:
1234
Threshold = 15

Output:
Digits Processed: 4 3 2 1
Sum = 10
Count = 4
Threshold Not Reached
'''

num = int(input("Enter number: "))
threshold = int(input("Enter threshold: "))

temp = num
sum = 0
count = 0
processed = ""

while temp > 0:
    digit = temp % 10   
    temp = temp // 10   
    
    sum += digit
    processed=processed+str(digit)
    count += 1
    
    if sum > threshold:
        break


print("Digits Processed:", *processed)
print("Sum =", sum)
print("Count =", count)

if sum > threshold:
    print("Threshold Exceeded")
else:
    print("Threshold Not Reached")
