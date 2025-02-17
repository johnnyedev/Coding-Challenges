def pali_num(num):
    num_list = []
    num_length = len(str(num))
    for i in str(num):
        num_list.append(i)

    index_count = 1
    for digit in num_list:
        if digit == num_list[num_length - index_count]:
            #print(f" {digit} matches {num_list[num_length - index_count]}")
            if num_length % 2 == 0 and index_count >= num_length / 2:
                #print(f"{num} is a palidrome")
                return True
            elif num_length % 2 != 0 and index_count >= num_length / 2:
                #print(f"{num} is a palidrome")
                return True
            index_count += 1
        else:
            #print(f"{num} is not a palidrome")
            return False

def largest_palindrome_product(num):
    product_list = set()
    for i in range(0, num + 1):
        counter = 0
        for n in range(0, num +1):
            product = i * counter
            #print(i, "multiplied by", counter, "=", product)

            is_palindrome = pali_num(product)
            if is_palindrome == True:
                product_list.add(product)
            counter += 1
    lpp = sorted(list(product_list))
    print(lpp[-1])


# product_num(99) # Largest Palindrome Product for 2 digits is 9009
largest_palindrome_product(999)  # Largest Palindrome Product for 3 digits is 906609
