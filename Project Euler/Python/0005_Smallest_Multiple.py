# Project Euler
# Problem 5: Smallest Multiple
# https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 

# Checks for the smallest multiple of 1-20
def smallest_multiple():
    large_num = 1_000_000_000_000_000_000_000_000_000_000_000
    for num in range(1, large_num):
        #print(num)
        if num % 1 == 0 and num % 2 == 0 and num % 3 == 0 and num % 4 == 0 and num % 5 == 0 and num % 6 == 0 and num % 7 == 0 and num % 8 == 0 and num % 9 == 0 and num % 10 == 0 and num % 11 == 0 and num % 12 == 0 and num % 13 == 0 and num % 14 == 0 and num % 15 == 0 and num % 16 == 0 and num % 17 == 0 and num % 18 == 0 and num % 19 == 0 and num % 20 == 0:
          print(f"{num} passed checks")
          return num

    return

smallest_multiple()

########## Example Output ##########
# 232792560 passed checks
