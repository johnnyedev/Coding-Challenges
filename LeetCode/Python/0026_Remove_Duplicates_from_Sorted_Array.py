# LeetCode
# Problem 26: Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
         
         nums_copy = nums.copy()
         for num in nums_copy:
            if nums.count(num) > 1:
                nums.remove(num)
                #print(f"removed duplicate: {num}")
