from typing import Optional


'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = []
        l2_list = []

        while l1:
            value = str(l1.val)
            l1_list.append(value)
            l1 = l1.next

        while l2:
            value = str(l2.val)
            l2_list.append(value)
            l2 = l2.next

        l1_num = int(''.join(l1_list[::-1]))
        l2_num = int(''.join(l2_list[::-1]))

        l3 = str(l1_num + l2_num)

        linked_list_l3 = None

        for num in l3:
            node = ListNode(int(num))
            if linked_list_l3 is None:
                linked_list_l3 = node
            else:
                node.next = linked_list_l3
                linked_list_l3 = node

        return linked_list_l3