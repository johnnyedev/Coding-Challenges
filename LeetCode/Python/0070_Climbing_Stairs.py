# LeetCode
# Problem 70: Climbing Stairs
# https://leetcode.com/problems/climbing-stairs


class Solution:
    def climbStairs(self, n: int) -> int:
        
        num = 0
        num_list = [1]
        for i in range(0, n): 
            num += num_list[i - 1]
            num_list.append(num)
        #print(num_list)
        return num_list[-1]
