s = 1 
while s <=3:
    print("Stundent",s,":") 
 
    subject = 1
    while subject <= 5:
        print(f"Subject {subject} ",end="")
       
        chap = 1 
        while chap <= 4:
            print(f"Chapter {chap} ",end="")
            chap+=1
        print()
        subject += 1
    s+=1
    print()