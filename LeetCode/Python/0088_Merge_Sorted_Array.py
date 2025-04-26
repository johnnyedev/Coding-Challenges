# LeetCode
# Problem 88: Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        for i in range(len(nums1)):
            if nums1[-1] == 0:
                nums1.pop()

        for i in range(len(nums2)):
            if nums2 != []:
                if nums2[-1] == 0:
                    nums2.pop()

        for i in range(len(nums2)):
            if nums2[i] != 0:
                nums1.append(nums2[i])

        while len(nums1) < (m + n):
            nums1.append(0)
        
        nums1.sort()   
