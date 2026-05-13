# SNAKE AND LADDER GAME USING MATCH CASE

import random

print("===== SNAKE AND LADDER GAME =====")

player1 = input("Enter Player 1 Name: ")
player2 = input("Enter Player 2 Name: ")

position1 = 0
position2 = 0

while True:

    # PLAYER 1 TURN

    print("\n------------------------")
    print(player1, "Turn")
    input("Press Enter To Roll Dice")

    dice = random.randint(1, 6)

    print("Dice Number =", dice)

    position1 = position1 + dice

    if position1 > 100:
        position1 = position1 - dice
        print("You Need Exact Number To Reach 100")

    print("Current Position =", position1)

    # MATCH CASE FOR PLAYER 1

    match position1:

        # LADDERS

        case 3:
            print("You Found A Ladder")
            position1 = 22

        case 8:
            print("You Found A Ladder")
            position1 = 26

        case 20:
            print("You Found A Ladder")
            position1 = 29

        case 28:
            print("You Found A Ladder")
            position1 = 55

        case 58:
            print("You Found A Ladder")
            position1 = 77

        # SNAKES

        case 17:
            print("Oops! Snake Bit You")
            position1 = 7

        case 54:
            print("Oops! Snake Bit You")
            position1 = 34

        case 62:
            print("Oops! Snake Bit You")
            position1 = 19

        case 98:
            print("Oops! Snake Bit You")
            position1 = 79

    print("New Position =", position1)

    # WIN CHECK PLAYER 1

    if position1 == 100:
        print("\n", player1, "Wins The Game")
        break

    # PLAYER 2 TURN

    print("\n------------------------")
    print(player2, "Turn")
    input("Press Enter To Roll Dice")

    dice = random.randint(1, 6)

    print("Dice Number =", dice)

    position2 = position2 + dice

    if position2 > 100:
        position2 = position2 - dice
        print("You Need Exact Number To Reach 100")

    print("Current Position =", position2)

    # MATCH CASE FOR PLAYER 2

    match position2:

        # LADDERS

        case 3:
            print("You Found A Ladder")
            position2 = 22

        case 8:
            print("You Found A Ladder")
            position2 = 26

        case 20:
            print("You Found A Ladder")
            position2 = 29

        case 28:
            print("You Found A Ladder")
            position2 = 55

        case 58:
            print("You Found A Ladder")
            position2 = 77

        # SNAKES

        case 17:
            print("Oops! Snake Bit You")
            position2 = 7

        case 54:
            print("Oops! Snake Bit You")
            position2 = 34

        case 62:
            print("Oops! Snake Bit You")
            position2 = 19

        case 98:
            print("Oops! Snake Bit You")
            position2 = 79

    print("New Position =", position2)

    # WIN CHECK PLAYER 2

    if position2 == 100:
        print("\n", player2, "Wins The Game")
        break