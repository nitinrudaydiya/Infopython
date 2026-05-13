'''
Assignment 8: Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0

'''


P = int(input("Principal = "))
R = int(input("Rate in % = "))
T = int(input("Time in years = "))

ci = (P*((1 + R/100)**T)-P)
amount = ci + P
print(f"Amount after interest = {amount}")