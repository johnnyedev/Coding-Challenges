# LeetCode
# Problem 20: Valid Parentheses
# https://leetcode.com/problems/valid-parentheses
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false
#
# Example 4:
# Input: s = "([])"
# Output: true
#
# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:

        my_stack = []
        for str in s:
            if len(s) < 2:
                return False
            if s[0] == ")" or s[0] == "]" or s[0] == "}":
                return False
            if s[-1] == "(" or s[-1] == "[" or s[-1] == "{":
                return False
            if str == "(" or str == "[" or str == "{":
                my_stack.append(str)
            if my_stack:
                if str == ")" and my_stack[-1] == "(":
                    my_stack.pop()
                elif str == ")":
                    return False
                elif str == "]" and my_stack[-1] == "[":
                    my_stack.pop()
                elif str == "]":
                    return False
                elif str == "}" and my_stack[-1] == "{":
                    my_stack.pop()
                elif str == "}":
                    return False
            else:
                if str == ")" or str == "]" or str == "}":
                    return False

            #print(str, my_stack)
            
        if my_stack == []:
            return True
        else:
            return False
        
        
        
