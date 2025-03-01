# LeetCode
# Problem 9: Palindrome Number
# https://leetcode.com/problems/palindrome-number

# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
# Constraints:
# -231 <= x <= 231 - 1

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x_str = str(x)
        end = len(x_str)
        end_counter = 1

        if len(x_str) == 1:
            is_palin = True
            return is_palin
        else:
            is_palin = None

        for i in range(floor(end / 2)):
            if x_str[i] == x_str[end - end_counter]:
                is_palin = True
                end_counter += 1
            else:
                is_palin = False
                return is_palin
        return is_palin
