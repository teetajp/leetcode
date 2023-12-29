# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # first node is head; (always defined)
        
        # we are creating a new list in place, from outside inwards
        
        # first, find the middle element (if it exists), as to divide the llist into first and second half
        # traverse through the second half of the llist and add nodes to a stack
        
        # create a new list by reassigning pointers by alternating between first and second list (stack), starting with first
        # middle element will belong to first list
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        queue = deque([])
        stack = []
    
        mid_idx = length // 2
        cur = head.next
        for i in range(1, length):
            if i <= mid_idx:
                queue.appendleft(cur)
            else:
                stack.append(cur)
            
            cur = cur.next
            
        cur = head
        for i in range(length - 1):
            if stack:
                cur.next = stack.pop()
                cur = cur.next
                
            if queue:
                cur.next = queue.pop()
                cur = cur.next
        cur.next = None
        return head