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

input_num_str = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"


def filter_num_str(input):

    input_list = list(input)
    grid_list = []
    row_list = []
    for i in range(0, len(input_list) - 1):
        if input_list[i] != " " and input_list[i+1] != " ":
            new_string = input_list[i] + input_list[i+1]
            row_list.append(new_string)
        if len(row_list) == 20:
                grid_list.append(row_list)
                row_list = []

#    print(grid_list)
    max_product_so_far = [0,0]

#### START Right Adajcent Calculation ####
    r_adj_list = []
    for row in range(0, 20):
        four_num = []
        for col in range(0, 17):
            for i in range(0, 4):
                four_num.append(grid_list[row][col + i])

            product = int(four_num[0])
            for i in range(1, 4):
                product *= int(four_num[i])

            four_num.append(product)
            r_adj_list.append(four_num)
            four_num = []

    for i in range(0, len(r_adj_list)):
        if r_adj_list[i][4] > max_product_so_far[1]:
            max_product_so_far[0] = r_adj_list[i]
            max_product_so_far[1] = r_adj_list[i][4]
#### END Right Adajacent Calculation ####

#### START Left Adajcent Calculation ####
    l_adj_list = []
    for row in range(0, 20):
        four_num = []
        for col in range(3, 20):
            for i in range(0, 4):
                four_num.append(grid_list[row][col - i])

            product = int(four_num[0])
            for i in range(1, 4):
                product *= int(four_num[i])

            four_num.append(product)
            l_adj_list.append(four_num)
            four_num = []

    for i in range(0, len(l_adj_list)):
        if l_adj_list[i][4] > max_product_so_far[1]:
            max_product_so_far[0] = l_adj_list[i]
            max_product_so_far[1] = l_adj_list[i][4]
#### END Left Adajacent Calculation ####

#### START Down Adajcent Calculation ####
    d_adj_list = []
    for row in range(0, 17):
        four_num = []
        for col in range(0, 20):
            for i in range(0, 4):
             #   print(grid_list[row + i][col])
                four_num.append(grid_list[row + i][col])
            #print("--------------------")

            product = int(four_num[0])
            for i in range(1, 4):
                product *= int(four_num[i])

            four_num.append(product)
            d_adj_list.append(four_num)
            four_num = []

    for i in range(0, len(d_adj_list)):
        if d_adj_list[i][4] > max_product_so_far[1]:
            max_product_so_far[0] = d_adj_list[i]
            max_product_so_far[1] = d_adj_list[i][4]
#### END Down Adajacent Calculation ####

#### START Up Adajcent Calculation ####
    u_adj_list = []
    for row in range(3, 20):
        four_num = []
        for col in range(0, 20):
            for i in range(0, 4):
                #print(grid_list[row - i][col])
                four_num.append(grid_list[row - i][col])
            #print("-----------------------")
            product = int(four_num[0])
            for i in range(1, 4):
                product *= int(four_num[i])

            four_num.append(product)
            u_adj_list.append(four_num)
            four_num = []

    for i in range(0, len(u_adj_list)):
        if u_adj_list[i][4] > max_product_so_far[1]:
            max_product_so_far[0] = u_adj_list[i]
            max_product_so_far[1] = u_adj_list[i][4]
#### END Up Adajacent Calculation ####

#### START Diagonal Down Right Adajcent Calculation ####
    ddr_adj_list = []
    for row in range(0, 17):
        four_num = []
        for col in range(0, 17):
            for i in range(0, 4):
                #print(grid_list[row + i][col + i])
                four_num.append(grid_list[row + i][col + i])
            #print("----------------------------------------")
            product = int(four_num[0])
            for i in range(1, 4):
                product *= int(four_num[i])

            four_num.append(product)
            ddr_adj_list.append(four_num)
            four_num = []

    for i in range(0, len(ddr_adj_list)):
        if ddr_adj_list[i][4] > max_product_so_far[1]:
            max_product_so_far[0] = ddr_adj_list[i]
            max_product_so_far[1] = ddr_adj_list[i][4]
#### END Diagonal Down Right Adajacent Calculation ####

#### START Diagonal Down Left Adajcent Calculation ####
    ddl_adj_list = []
    for row in range(0, 17):
        four_num = []
        for col in range(3, 20):
            for i in range(0, 4):
                #print(grid_list[row + i][col - i])
                four_num.append(grid_list[row + i][col - i])
            #print("----------------------------------------")
            product = int(four_num[0])
            for i in range(1, 4):
                product *= int(four_num[i])

            four_num.append(product)
            ddl_adj_list.append(four_num)
            four_num = []

    for i in range(0, len(ddl_adj_list)):
        if ddl_adj_list[i][4] > max_product_so_far[1]:
            max_product_so_far[0] = ddl_adj_list[i]
            max_product_so_far[1] = ddl_adj_list[i][4]
#### END Diagonal Down Left Adajacent Calculation ####

#### START Diagonal Up Right Adajcent Calculation ####
    dur_adj_list = []
    for row in range(3, 20):
        four_num = []
        for col in range(0, 17):
            for i in range(0, 4):
                #print(grid_list[row - i][col + i])
                four_num.append(grid_list[row - i][col + i])
            #print("----------------------------------------")
            product = int(four_num[0])
            for i in range(1, 4):
                product *= int(four_num[i])

            four_num.append(product)
            dur_adj_list.append(four_num)
            four_num = []

    for i in range(0, len(dur_adj_list)):
        if dur_adj_list[i][4] > max_product_so_far[1]:
            max_product_so_far[0] = dur_adj_list[i]
            max_product_so_far[1] = dur_adj_list[i][4]
#### END Diagonal Up Right Adajacent Calculation ####

#### START Diagonal Up Left Adajcent Calculation ####
    dul_adj_list = []
    for row in range(3, 20):
        four_num = []
        for col in range(3, 20):
            for i in range(0, 4):
                #print(grid_list[row - i][col - i])
                four_num.append(grid_list[row - i][col - i])
            #print("----------------------------------------")
            product = int(four_num[0])
            for i in range(1, 4):
                product *= int(four_num[i])

            four_num.append(product)
            dul_adj_list.append(four_num)
            four_num = []

    for i in range(0, len(dul_adj_list)):
        if dul_adj_list[i][4] > max_product_so_far[1]:
            max_product_so_far[0] = dul_adj_list[i]
            max_product_so_far[1] = dul_adj_list[i][4]
#### END Diagonal Up Left Adajacent Calculation ####

    print(f"These four adjacent numbers: {max_product_so_far[0]} produce the largest product: {max_product_so_far[1]}")

filter_num_str(input_num_str)

########## Example Output ##########
# These four adjacent numbers: ['89', '94', '97', '87', 70600674] produce the largest product: 70600674
