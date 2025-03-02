# LeetCode
# Problem 13: Roman to Integer
# https://leetcode.com/problems/roman-to-integer

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
# The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 
# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].
############

# To determine the amount to subtract:
# IV = I(1)   + V(5)    =    6 -   IV(4) =   2
# IX = I(1)   + X(10)   =   11 -   IX(9) =   2
# XL = X(10)  + L(50)   =   60 -  XL(40) =  20
# XC = X(10)  + C(100)  =  110 -  XC(90) =  20 
# CD = C(100) + D(500)  =  600 - CD(400) = 200
# CM = C(100) + M(1000) = 1100 - CM(900) = 200

class Solution:
    def romanToInt(self, s: str) -> int:

        total_val = 0
        for i in range(len(s)):
            if s[i] == "I":
                total_val += 1
            elif s[i] == "V":
                total_val += 5
            elif s[i] == "X":
                total_val += 10
            elif s[i] == "L":
                total_val += 50
            elif s[i] == "C":
                total_val += 100
            elif s[i] == "D":
                total_val += 500
            elif s[i] == "M":
                total_val += 1000

        total_sub = 0
        if "IV" in s or "IX" in s:
            total_sub += 2
        if "XL" in s or "XC" in s:
            total_sub += 20
        if "CD" in s or "CM" in s:
            total_sub += 200

        final_num = total_val - total_sub

        return final_num
