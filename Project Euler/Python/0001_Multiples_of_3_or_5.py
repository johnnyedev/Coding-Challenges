# Project Euler
# Problem 1: Multiples of 3 or 5
# https://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the Sum of all the multiples of 3 or 5 below 1000

number = 1000
mysum = 0

for i in range(number):
    if i % 3 == 0 or i % 5 == 0:
        mysum += i

print(mysum)

########### Example Output ###########
# 233168
