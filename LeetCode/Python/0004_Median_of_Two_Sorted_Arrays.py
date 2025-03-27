# LeetCode
# Problem 4: Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num_list = []
        for num in nums1:
            num_list.append(num)
        
        for num in nums2:
            num_list.append(num)

        return median(num_list)
