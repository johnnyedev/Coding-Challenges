# Project Euler
# Problem 9: Special Pythagorean Triplet
# https://projecteuler.net/problem=9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 =  9 + 16 = 25 = 5^2

# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product abc




# Starting with 1, the first set of numbers that could sum to 1000 are: 1, 2, 997
# Lets find every number that could be added where a < b < c that a + b + c = 1000

def find_ptriplet():

    for a in range(1, 997):
        for b in range(2, 997):
            c = 1000 - (a + b)
            if a < b and b < c:
                #print(f"checking numbers: {a}, {b}, {c}")
                if a + b + c == 1000:
                    #print(f"{a} + {b} + {c} = 1000")
                    a_exp = a * a
                    b_exp = b * b
                    c_exp = c * c
                    ae_be = a_exp + b_exp
                    #print(f"check if {a_exp} + {b_exp} = {ae_be} = {c_exp}")
                    if a_exp + b_exp == c_exp:
                        print(f"Found: {a}+{b}+{c} = 1000 and a^2 {a_exp} + b^2 {b_exp} = {ae_be} = c^2 {c_exp}")
                        product = a * b * c
                        print(f"Product of abc = {product}")

find_ptriplet()


########## Example Output ##########
# Found: 200+375+425 = 1000 and a^2 40000 + b^2 140625 = 180625 = c^2 180625
# Product of abc = 31875000
