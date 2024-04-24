'''
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, val):
        new_node = ListNode(val)
        cur_node = self.head

        if not cur_node:
            self.head = new_node
            return
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node

    def reverseList(self):
        new = None
        cur_node = self.head
        while cur_node:
            next_node = cur_node.next
            cur_node.next = new
            new = cur_node
            cur_node = next_node
        return new


sol = LinkedList()
sol.append_node(1)
sol.append_node(2)
sol.append_node(3)
print(sol.reverseList())
