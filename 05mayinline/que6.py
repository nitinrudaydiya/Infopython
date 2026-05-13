'''
6.
Data Validation System – Character Identifier
A system needs to validate user input characters.
If the input is:
Alphabet → display "Alphabet"
Digit → display "Digit"
Otherwise → display "Special Character"
Write a program using inline if to classify the character.
'''

n = input("Enter the character : ")

print("Alphabet" if n in "abcdefghijklmnopqrstuvwxyz" else "Digit" if n in "1234567890" else "Special Character")