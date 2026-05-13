
# SMART ONLINE EXAMINATION SYSTEM


import random

print("        SMART ONLINE EXAMINATION SYSTEM")

# LOGIN SYSTEM

username = "admin"
password = "1234"

attempt = 0

while attempt < 3:

    user = input("\nEnter Username: ")
    pwd = input("Enter Password: ")

    if user == username and pwd == password:

        print("\nLogin Successful")
        break

    else:

        print("Invalid Username or Password")

    attempt = attempt + 1

if attempt == 3:

    print("\nToo Many Wrong Attempts")
    exit()

# STUDENT DETAILS

name = input("\nEnter Student Name: ")
roll = input("Enter Roll Number: ")

history = []

# MAIN LOOP

while True:

    print("                  MAIN MENU")

    print("1. Start Exam")
    print("2. Exam Instructions")
    print("3. View Previous Result")
    print("4. Exit")

    choice = int(input("\nEnter Your Choice: "))


    match choice:

        # START EXAM

        case 1:

            score = 0

            print("<------SUBJECT SELECTION------>")

            print("1. Python")
            print("2. General Knowledge")
            print("3. Mathematics")

            subject = int(input("\nSelect Subject: "))


            if subject == 1:

                print("\nPython Exam Started")

                # QUESTION 1

                print("\nQ1. Who developed Python?")

                print("1. Dennis Ritchie")
                print("2. Guido van Rossum")
                print("3. James Gosling")
                print("4. Charles Babbage")

                answer = int(input("Enter Answer: "))

                if answer == 2:

                    print("Correct Answer")
                    score = score + 1

                else:

                    print("Wrong Answer")

                # QUESTION 2

                print("\nQ2. Which symbol is used for comments?")

                print("1. //")
                print("2. <!-- -->")
                print("3. #")
                print("4. *")

                answer = int(input("Enter Answer: "))

                if answer == 3:

                    print("Correct Answer")
                    score = score + 1

                else:

                    print("Wrong Answer")

                # QUESTION 3

                print("\nQ3. Which loop is used in Python?")

                print("1. for")
                print("2. while")
                print("3. both")
                print("4. none")

                answer = int(input("Enter Answer: "))

                if answer == 3:

                    print("Correct Answer")
                    score = score + 1

                else:

                    print("Wrong Answer")

                # QUESTION 4

                print("\nQ4. Which keyword is used for conditions?")

                print("1. if")
                print("2. when")
                print("3. case")
                print("4. select")

                answer = int(input("Enter Answer: "))

                if answer == 1:

                    print("Correct Answer")
                    score = score + 1

                else:

                    print("Wrong Answer")

                # QUESTION 5

                print("\nQ5. Which data type stores decimal values?")

                print("1. int")
                print("2. float")
                print("3. str")
                print("4. bool")

                answer = int(input("Enter Answer: "))

                if answer == 2:

                    print("Correct Answer")
                    score = score + 1

                else:

                    print("Wrong Answer")

            # GENERAL KNOWLEDGE EXAM

            elif subject == 2:

                print("\nGeneral Knowledge Exam Started")

                print("\nQ1. Capital of India?")

                print("1. Mumbai")
                print("2. Delhi")
                print("3. Chennai")
                print("4. Kolkata")

                answer = int(input("Enter Answer: "))

                if answer == 2:

                    print("Correct Answer")
                    score = score + 1

                else:

                    print("Wrong Answer")

                print("\nQ2. National Animal of India?")

                print("1. Lion")
                print("2. Tiger")
                print("3. Elephant")
                print("4. Horse")

                answer = int(input("Enter Answer: "))

                if answer == 2:

                    print("Correct Answer")
                    score = score + 1

                else:

                    print("Wrong Answer")

                print("\nQ3. Largest Planet?")

                print("1. Earth")
                print("2. Mars")
                print("3. Jupiter")
                print("4. Venus")

                answer = int(input("Enter Answer: "))

                if answer == 3:

                    print("Correct Answer")
                    score = score + 1

                else:

                    print("Wrong Answer")

                print("\nQ4. Who is known as Father of Nation?")

                print("1. Nehru")
                print("2. Gandhi")
                print("3. Patel")
                print("4. Bose")

                answer = int(input("Enter Answer: "))

                if answer == 2:

                    print("Correct Answer")
                    score = score + 1

                else:

                    print("Wrong Answer")

                print("\nQ5. Which is the national flower of India?")

                print("1. Rose")
                print("2. Lotus")
                print("3. Lily")
                print("4. Sunflower")

                answer = int(input("Enter Answer: "))

                if answer == 2:

                    print("Correct Answer")
                    score = score + 1

                else:

                    print("Wrong Answer")

            # MATHEMATICS EXAM

            elif subject == 3:

                print("\nMathematics Exam Started")

                a = random.randint(1, 20)
                b = random.randint(1, 20)

                answer = int(input(f"\nQ1. {a} + {b} = "))

                if answer == a + b:

                    print("Correct Answer")
                    score = score + 1

                else:

                    print("Wrong Answer")

                a = random.randint(1, 2000)
                b = random.randint(1, 2000)

                answer = int(input(f"\nQ2. {a} - {b} = "))

                if answer == a - b:

                    print("Correct Answer")
                    score = score + 1

                else:

                    print("Wrong Answer")

                a = random.randint(1, 100)
                b = random.randint(1, 100)

                answer = int(input(f"\nQ3. {a} x {b} = "))

                if answer == a * b:

                    print("Correct Answer")
                    score = score + 1

                else:

                    print("Wrong Answer")

            else:

                print("Invalid Subject")
                continue

            # RESULT SECTION

            percentage = (score / 3) * 100

            print("\n=================================================")
            print("                    RESULT")
            print("=================================================")

            print("Student Name :", name)
            print("Roll Number  :", roll)
            print("Marks         :", score)
            print("Percentage    :", percentage)

            if percentage >= 80:

                print("Grade : A")
                print("Excellent")

            elif percentage >= 60:

                print("Grade : B")
                print("Good")

            elif percentage >= 40:

                print("Grade : C")
                print("Average")

            else:

                print("Grade : F")
                print("Fail")

            history.append(score)

        # INSTRUCTIONS

        case 2:

            print("---->EXAM INSTRUCTIONS<----")

            print("1. Read Questions Carefully")
            print("2. Each Question Carries 1 Mark")
            print("3. No Negative Marking")
            print("4. Do Not Close Program During Exam")
            print("5. Enter Correct Option Number")

        # VIEW PREVIOUS RESULT

        case 3:

            print("--->PREVIOUS RESULTS<---")

            if len(history) == 0:

                print("No Exam History Available")

            else:

                count = 1

                for i in history:

                    print("Attempt", count, "=", i, "Marks")

                    count = count + 1

        case 4:

            print("\nThank You For Using Exam System")

            break

        case _:

            print("Invalid Choice")