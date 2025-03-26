# LeetCode
# Problem 69: Sqrt(x)
# https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:

        for i in range(x + 1):
            result = i * i
            #print(result, i)
            if result == x:
                return i
            if result > x:
                return i - 1     
        return x
