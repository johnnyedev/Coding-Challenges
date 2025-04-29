# LeetCode
# Problem 8: String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi

class Solution:
    def myAtoi(self, s: str) -> int:

        str_list = []
        type = None
        zero = False
        for str in s:
            if not str.isspace():
                
                #print(f"debug: type:{type} zero:{zero} str:{str}")
                if type == None and zero == True and (str == '+' or str == '-'):
                    result = 0
                    break
                elif type == None and str == '+':
                    if not str_list:
                        type = "pos"
                    else:
                        break
                elif type == None and str == '-':
                    if not str_list:
                        type = "neg"
                    else:
                        break
                elif str.isalpha() or not str.isdigit():
                    #print("alpha/non-digit char found, stop")
                    if not str_list:
                        result = 0
                        break
                    else:
                        break
                elif str.isdigit():
                    #print(f"string list: {str_list}")
                    if str == '0' and not str_list:
                        #print("leading 0, skip")
                        zero = True
                        pass
                    elif str == '0' and str_list[-1].isdigit():
                        str_list.append(str)
                    elif str != '0':
                        #print(f"adding {str} to string list")
                        str_list.append(str)

            elif str.isspace() and (type != None or zero == True or str_list):
                result = 0
                break
            

        
       #print(type)
       #print(str_list)

        if not str_list:
            result = 0
        elif type == 'neg':
            result = int('-' + ''.join(str_list))
        else:
            result = int(''.join(str_list))

        if result < -2**31:
            result = -2**31
        elif result > 2**31 - 1:
            result = 2**31 - 1
        #print(f"2 to 31st == {2**31}")
        
        return result
