# LeetCode
# Problem 3: Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        my_list = []
        counts = []
        clone = []
        for str in s:
            clone.append(str)

        if len(clone) >= 130:
            clone = list(set(clone))
        print(clone)

        while len(clone) > 0:
            string = []
            for char in clone:
                string += char

            for str in string:
                if str not in my_list:
                    #print(f"adding {str}")
                    my_list.append(str)
                elif str in my_list:
                    #print(f"count added: {len(my_list)}")
                    counts.append(len(my_list))
                    #print(f"clearing {my_list}")
                    my_list = []
            counts.append(len(my_list))
            del clone[0]
            #print(f"clone looks like {clone}")
            #print(f"clearing {my_list}")
            my_list = []

        max_so_far = 0
        for num in counts:
            if num > max_so_far:
                max_so_far = num 
        
        #print(my_list, counts, max_so_far)
        return max_so_far
