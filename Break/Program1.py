i = 1 
while i <=10:
    print(i)
    if i == 5:
        print("Banda mil gaya")
        break 
    i += 1


for i in range(1,11):
    print(i)
    if i == 5:
        print("Banda mil gaya")
        break

while True:
    password = input("Enter the Password : ").lower()
    if password == "admin":
        print("Access Granted")
        break
    else:
        print("Enter correct password")