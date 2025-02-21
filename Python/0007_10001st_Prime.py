# Project Euler
# Problem 7: 10001st Prime
# https://projecteuler.net/problem=7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?


# Check if number is Prime
def is_prime(number):
    if number > 1:
        for i in range(2, number):
            result = number % i
            if result == 0:
                return False
        return True
    else:
        return False


# Gather 10,001 Prime Numbers
def nth_prime_number(number):
    prime_list = []
    prime_count = 0
    loop_iteration = 1
    while prime_count < number:

        if is_prime(loop_iteration) == True:
            prime_list.append(loop_iteration)
            prime_count += 1

        loop_iteration += 1

    #print(prime_list)
    last_prime = prime_list[-1]
    last_prime_index = prime_list.index(last_prime) + 1

    output1 = print(f"Last Prime Number is: {last_prime}")
    output2 = print(f"In Position: {last_prime_index}")

    return output1, output2


nth_prime_number(10001)


########## Example Output ##########

# Last Prime Number is: 104743
# In Position: 10001
