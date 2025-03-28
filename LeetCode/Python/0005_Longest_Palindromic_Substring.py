# LeetCode
# Problem 5: Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        p_list = [""]
        count = 0
        for str in s:
            my_list = list(s[count::1])
            if len(p_list[0]) >= len(my_list):
                return p_list[0]
            for i in range(len(s)):
                if len(p_list[0]) >= len(my_list):
                    break
                elif my_list == my_list[::-1]:
                    p_list = ["".join(my_list)]
                else:
                    my_list.pop()
            count += 1
        return p_list[0]
