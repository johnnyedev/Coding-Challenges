# LeetCode
# Problem 14: Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_so_far = float(inf)
        for str in strs:
            if len(str) < min_so_far:
                min_so_far = len(str)
                smallest_str = str
        #print(smallest_str)
        
        my_string = ""
        count = 0
        for ltr in smallest_str:
            match_count = 0
            for i in range(len(strs)):
                #print(f"{ltr} comparing to {strs[i]}:{strs[i][count]}")
                if ltr == strs[i][count]:
                    match_count += 1
                    #print(f"match {match_count} : {len(strs)}")
                    if len(smallest_str) == 1 and match_count == len(strs):
                        my_string = ltr
                    elif match_count == len(strs):
                        my_string += ltr
                else:
                    return my_string
            count += 1
        #print(my_string)
        return my_string
