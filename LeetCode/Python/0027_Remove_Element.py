# LeetCode
# Problem 27: Remove Element
# https://leetcode.com/problems/remove-element


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        result_list = nums.copy()
        for num in result_list:
            if num == val:
                nums.remove(num)
 #       print(nums)
 #       print(result_list)
        return len(nums)
