# Project Euler
# Problem 11: Largest Product in a Grid
# https://projecteuler.net/problem=11

# In the 20 x 20 grid below, four numbers along a diagonal line have been marked in red. (quoted in these comments)
#
# 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10"26"38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95"63"94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17"78"78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35"14"00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
#
# The product of these numbers is 26 X 63 X 78 X 14 = 1788696
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20 x 20 grid?


# If we take the largest number that surrounds each of the quoted numbers that would be: 26(95), 63(97), 78(94), 14(96)
# So this script needs to first parse the above grid as an input number and then filter down to those 4 numbers from surrounding 8 numbers
#                   Rel Col Position
# Row Above is:      -21, -20, -19
# Side by side is:    -1,   0,   1
# Row Below is:     ++19, +20, +21


input_num_str = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"


def filter_num_str(input):

    input_list = list(input)
    grid_list = []
    for i in range(0, len(input_list)-1):
        if input_list[i] != " " and input_list[i+1] != " ":
            new_string = input_list[i] + input_list[i+1]
            grid_list.append(new_string)
    print("Our number grid converted to a list with spaces removed:")
    print(grid_list)

    index_list = [grid_list.index("26")]
    for i in range(0, 3):
        index_list.append(int(index_list[i]) + 21)
    print(f"Index locations of our four numbers 26, 63, 78, 14: {index_list}")


    largest_adj = []
    for index in index_list:
        adjacent_nums = []
        adjacent_nums.append(grid_list[index - 21])
        adjacent_nums.append(grid_list[index - 20])
        adjacent_nums.append(grid_list[index - 19])
        adjacent_nums.append(grid_list[index - 1])
        adjacent_nums.append(grid_list[index + 1])
        adjacent_nums.append(grid_list[index + 19])
        adjacent_nums.append(grid_list[index + 20])
        adjacent_nums.append(grid_list[index + 21])
        largest_adj.append(sorted(adjacent_nums).pop())
    print(f"Largest four adjacent numbers: {largest_adj}")

    product = int(largest_adj[0])
    for i in range(1, 4):
        product *= int(largest_adj[i])
    print(f"Our final product is: {product}")


filter_num_str(input_num_str)

#### FAILURE ####
# The issue with this script is that I misunderstood the task!
# I thought for the given red numbers (quoted in the comment at the top) you were supposed to gather their adjacent numbers
# And then find the largest product, which is what this script does... (see below example output)
# You're really suppose to go through the entire grid and find every possible 4 sequencs of numbers... 
# left, down, up, right, diagonally and which sequence produces the largest product -facepalm- (working on V2 of script now)


########### Example Output ##########
# Our number grid converted to a list with spaces removed:
# ['08', '02', '22', '97', '38', '15', '00', '40', '00', '75', '04', '05', '07', '78', '52', '12', '50', '77', '91', '08', '49', '49', '99', '40', '17', '81', '18', '57', '60', '87', '17', '40', '98', '43', '69', '48', '04', '56', '62', '00', '81', '49', '31', '73', '55', '79', '14', '29', '93', '71', '40', '67', '53', '88', '30', '03', '49', '13', '36', '65', '52', '70', '95', '23', '04', '60', '11', '42', '69', '24', '68', '56', '01', '32', '56', '71', '37', '02', '36', '91', '22', '31', '16', '71', '51', '67', '63', '89', '41', '92', '36', '54', '22', '40', '40', '28', '66', '33', '13', '80', '24', '47', '32', '60', '99', '03', '45', '02', '44', '75', '33', '53', '78', '36', '84', '20', '35', '17', '12', '50', '32', '98', '81', '28', '64', '23', '67', '10', '26', '38', '40', '67', '59', '54', '70', '66', '18', '38', '64', '70', '67', '26', '20', '68', '02', '62', '12', '20', '95', '63', '94', '39', '63', '08', '40', '91', '66', '49', '94', '21', '24', '55', '58', '05', '66', '73', '99', '26', '97', '17', '78', '78', '96', '83', '14', '88', '34', '89', '63', '72', '21', '36', '23', '09', '75', '00', '76', '44', '20', '45', '35', '14', '00', '61', '33', '97', '34', '31', '33', '95', '78', '17', '53', '28', '22', '75', '31', '67', '15', '94', '03', '80', '04', '62', '16', '14', '09', '53', '56', '92', '16', '39', '05', '42', '96', '35', '31', '47', '55', '58', '88', '24', '00', '17', '54', '24', '36', '29', '85', '57', '86', '56', '00', '48', '35', '71', '89', '07', '05', '44', '44', '37', '44', '60', '21', '58', '51', '54', '17', '58', '19', '80', '81', '68', '05', '94', '47', '69', '28', '73', '92', '13', '86', '52', '17', '77', '04', '89', '55', '40', '04', '52', '08', '83', '97', '35', '99', '16', '07', '97', '57', '32', '16', '26', '26', '79', '33', '27', '98', '66', '88', '36', '68', '87', '57', '62', '20', '72', '03', '46', '33', '67', '46', '55', '12', '32', '63', '93', '53', '69', '04', '42', '16', '73', '38', '25', '39', '11', '24', '94', '72', '18', '08', '46', '29', '32', '40', '62', '76', '36', '20', '69', '36', '41', '72', '30', '23', '88', '34', '62', '99', '69', '82', '67', '59', '85', '74', '04', '36', '16', '20', '73', '35', '29', '78', '31', '90', '01', '74', '31', '49', '71', '48', '86', '81', '16', '23', '57', '05', '54', '01', '70', '54', '71', '83', '51', '54', '69', '16', '92', '33', '48', '61', '43', '52', '01', '89', '19', '67', '48']
# Index locations of our four numbers 26, 63, 78, 14: [128, 149, 170, 191]
# Largest four adjacent numbers: ['95', '97', '94', '96']
# Our final product is: 83156160
