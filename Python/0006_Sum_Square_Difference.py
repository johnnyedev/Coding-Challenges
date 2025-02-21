# Project Euler
# Problem 6: Sum Square Difference
# https://projecteuler.net/problem=6

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + . . . + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + . . . + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sum_sq(num):
    square_list = []
    for i in range(1, num + 1):
        square = i * i
        #print(f"{i} * {i} = {square}")
        square_list.append(square)
    #print(square_list)
    square_sum = 0
    for i in range(0, len(square_list)):
        square_sum += square_list[i]
        #print(square_sum)
    return square_sum

def sq_sum(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    #print(sum)
    sum_sq = sum * sum
    #print(sum_sq)
    return sum_sq


# Set the input num to desired value
input_num = 100
sum_of_squares = sum_sq(input_num)
square_of_sums = sq_sum(input_num)


print(square_of_sums - sum_of_squares)

########## Example Output ##########
# 25164150
