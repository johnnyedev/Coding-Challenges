# Project Euler
# Problem 3: Largest Prime Factor
# https://projecteuler.net/problem=3

# The prime factors of 13195 are 5, 7, 13, and 29.
# What is the largest prime factor of the number 600851475143 ?



# V2 This one reduces workload as once it loops to a point where a new factor = the previous factors result, we know there are no more factors. See Example Output below
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
    factor_results = [0]
    print(f"Looking for factors of: {number}")
    print(f"--------------------------------------------")
    
    for factor in range(1, number):
        if number % factor == 0:
            result1 = number / factor
            print(f"Factor Found: {number} / {factor} = {result1}")
            
            #print(factor, "==", factor_results[-1])
            if factor == factor_results[-1]:
                #print ("no more factors")
                for i in range(2):
                    del factor_results[0]
                factor_results.reverse()
                
                factors_list = factors_list + factor_results
                
                return factors_list
            
            factor_results.append(int(result1))
            factors_list.append(factor)
            
def check_prime_factors(factors):
    prime_factor_list = []
    
    for num in factors:
        prime_factors = is_prime(num)
        #print(f"Is {num} a prime number?: {prime_factors}")
        if prime_factors == True:
            prime_factor_list.append(num)
    return prime_factor_list

    

    
# Set this number
number = 13195
factors = check_factors(number)
prime_factors = check_prime_factors(factors)

print(f"Factors: {factors}")
print(f"Prime Factors: {prime_factors}")
print(f"Largest Prime Factor: {prime_factors[-1]}")


########## Example Output ##########
# Looking for factors of: 13195
# --------------------------------------------
# Factor Found: 13195 / 1 = 13195.0
# Factor Found: 13195 / 5 = 2639.0
# Factor Found: 13195 / 7 = 1885.0
# Factor Found: 13195 / 13 = 1015.0
# Factor Found: 13195 / 29 = 455.0
# Factor Found: 13195 / 35 = 377.0
# Factor Found: 13195 / 65 = 203.0
# Factor Found: 13195 / 91 = 145.0
# Factor Found: 13195 / 145 = 91.0
# Factors: [1, 5, 7, 13, 29, 35, 65, 91, 145, 203, 377, 455, 1015, 1885, 2639]
# Prime Factors: [5, 7, 13, 29]
# Largest Prime Factor: 29

