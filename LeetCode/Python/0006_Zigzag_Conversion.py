# LeetCode
# Problem 6: Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
            
        char_list = [''] * numRows

        curr = 0
        step = 0

        for char in s:
            #print(curr)
            char_list[curr] += char

            if curr == 0 and numRows > 1:
                step = 1
            elif curr != 0 and curr == numRows - 1:
                step = -1

            curr += step

        result = ''.join(char_list)
        #print(result)
        return result
