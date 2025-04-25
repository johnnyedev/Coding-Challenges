# LeetCode
# Problem 27: Remove Element
# https://leetcode.com/problems/remove-element


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        list_copy = nums.copy()
        for num in list_copy:
            if num == val:
                nums.remove(num)
        #print(nums)
        #print(list_copy)
