# LeetCode
# Problem 1: Two Sum
# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
#
# Only one valid answer exists.
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Print statments cause "Output Limit Exceeded" Error on leetcode...
        # ... when the nums list is really long. So commented them all out.

        index_list = []
        num_count1 = 0
        #print(f"Index Length: {len(nums) - 1}")
        for num in nums:
            #print(num)
            num_count2 = 0
            for i in range(0, len(nums) -1):
                
                #print(f"Indexes: {num_count1} + {num_count2}")
                if num_count1 != num_count2:
                    sum = num + nums[num_count2]
                    #print(f"{num} + {nums[num_count2]} = {sum}")
                
                    if sum == target:
                        index_list.append(num_count1)
                        index_list.append(num_count2)
                        #print(index_list)
                        return sorted(index_list)
               # else:
                    #print("Dont add the same indexes together")
                num_count2 += 1
                #print("-----------------------------------------")
            num_count1 += 1
