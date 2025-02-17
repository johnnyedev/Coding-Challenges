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
