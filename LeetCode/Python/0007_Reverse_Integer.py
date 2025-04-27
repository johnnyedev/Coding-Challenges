# LeetCode
# Problem 7: Reverse Integer
# https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        
        val = str(x)
        rev = val[::-1]

        if rev[-1] == '-':
            rev = '-' + rev[:-1]
        
        result = int(rev)

        if result > 2**31 - 1 or result < -2**31:
            result = 0

        return result
