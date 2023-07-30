# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        # while we are still iterating (possibly stuck in cycle)
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow: # pointers met in the cycle
                return True
            
        return False