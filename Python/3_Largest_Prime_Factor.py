def is_prime(number):
    if number > 1:
        for i in range(2, number):
            result = number % i
            if result == 0:
                return False
        return True
    else:
        return False


def check_factors(number):
    factors_list = []
    prime_factors_list = []
    print(f"Looking for factors of: {number}")
    print(f"--------------------------------------------")
    
    for factor in range(1, number):
        if number % factor == 0:
            result1 = number / factor
            print(f"Factor Found: {number} / {factor} = {result1}")
            factors_list.append(factor)
            
            result2 = is_prime(factor)
            print(f"Is Factor Prime?: {result2}")
            print(f"--------------------------------------------")
            if result2 == True:
                prime_factors_list.append(factor)
            
    return factors_list, prime_factors_list        

    
# Set this number
number = 13195
results = check_factors(number)


print(f"Is {number} Prime?: {is_prime(number)}")
print(f"Factors: {results[0]}")
print(f"Prime Factors: {results[1]}")
print(f"Largest Prime Factor: {results[1][-1]}")



######## Example Output ########

# Looking for factors of: 13195
# --------------------------------------------
# Factor Found: 13195 / 1 = 13195.0
# Is Factor Prime?: False
# --------------------------------------------
# Factor Found: 13195 / 5 = 2639.0
# Is Factor Prime?: True
# --------------------------------------------
# Factor Found: 13195 / 7 = 1885.0
# Is Factor Prime?: True
# --------------------------------------------
# Factor Found: 13195 / 13 = 1015.0
# Is Factor Prime?: True
# --------------------------------------------
# Factor Found: 13195 / 29 = 455.0
# Is Factor Prime?: True
# --------------------------------------------
# Factor Found: 13195 / 35 = 377.0
# Is Factor Prime?: False
# --------------------------------------------
# Factor Found: 13195 / 65 = 203.0
# Is Factor Prime?: False
# --------------------------------------------
# Factor Found: 13195 / 91 = 145.0
# Is Factor Prime?: False
# --------------------------------------------
# Factor Found: 13195 / 145 = 91.0
# Is Factor Prime?: False
# --------------------------------------------
# Factor Found: 13195 / 203 = 65.0
# Is Factor Prime?: False
# --------------------------------------------
# Factor Found: 13195 / 377 = 35.0
# Is Factor Prime?: False
# --------------------------------------------
# Factor Found: 13195 / 455 = 29.0
# Is Factor Prime?: False
# --------------------------------------------
# Factor Found: 13195 / 1015 = 13.0
# Is Factor Prime?: False
# --------------------------------------------
# Factor Found: 13195 / 1885 = 7.0
# Is Factor Prime?: False
# --------------------------------------------
# Factor Found: 13195 / 2639 = 5.0
# Is Factor Prime?: False
# --------------------------------------------
# Is 13195 Prime?: False
# Factors: [1, 5, 7, 13, 29, 35, 65, 91, 145, 203, 377, 455, 1015, 1885, 2639]
# Prime Factors: [5, 7, 13, 29]
# Largest Prime Factor: 29
