'''
2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17
'''


num = int(input("Enter the num : "))

while True:
    num += 1
    count = 0
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            count += 1
            break
        
    
    if num > 1 and count == 0:
        print("Next Prime =", num)
        break