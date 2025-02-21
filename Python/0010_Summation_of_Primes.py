# Project Euler
# Problem 10: Summation of Primes
# https://projecteuler.net/problem=10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. 
# Find the sum of all the primes below two million.


def is_prime(number):
    if number > 1:
        for i in range(2, number):
            result = number % i
            if result == 0:
                return False
        return True
    else:
        return False


def sum_of_primes(number):
    prime_list = []
    for num in range(0, number):
        if_prime = is_prime(num)
        if if_prime:
            #print(f"{num} is prime")
            prime_list.append(num)
    #print(f"Prime List: {prime_list}")

    prime_sum = 0
    for i in range(0, len(prime_list)):
        prime_sum += prime_list[i]
    print(f"Sum of Primes: {prime_sum}")


# sum_of_primes(10) # equals 17
sum_of_primes(2_000_000)

########## Example Output ##########
# Sum of Primes: 142913828922
