from typing import Optional


'''
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
Follow up: Could you do this in one pass?
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        prev = cur
        length = self.size(head)
        ind = 0
        while cur:
            if length - n == ind:
                if ind == 0:
                    head = cur.next
                else:
                    prev.next = cur.next
                return head
            ind += 1
            prev = cur
            cur = cur.next

    def size(self, head):
        cur = head
        ind = 0
        while cur:
            cur = cur.next
            ind += 1
        return ind