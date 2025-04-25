# LeetCode
# Problem 125: Valid Palindrome
# https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_list = []
        for char in s:
            if char.isalnum():
                char_list.append(char.lower())
 
        result = False
        if char_list == []:
            result = True
        
        count = 1
        for char in char_list:
            #print(f"compare: {char}:{char_list[-count]}")
            if char == char_list[-count]:
                result = True
            else:
                return False
            count += 1
        return result
