# LeetCode
# Problem 2: Add Two Numbers
# https://leetcode.com/problems/add-two-numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example 1
# 2 -> 4 -> 3
# 5 -> 6 -> 4
# -----------
# 7 -> 0 -> 8
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        linked_list_one = l1
        num_one = ""

        while linked_list_one:
            num_one += str(linked_list_one.val)
            linked_list_one = linked_list_one.next

        linked_list_two = l2
        num_two = ""

        while linked_list_two:
            num_two += str(linked_list_two.val)
            linked_list_two = linked_list_two.next           
             
        result = int(num_one[::-1]) + int(num_two[::-1])
        result_list = []
        for num in reversed(str(result)):
            result_list.append(int(num))

        head = ListNode(result_list[0])
        curr = head
        for num in result_list[1:]:
            curr.next = ListNode(num)
            curr = curr.next
            
        return head
