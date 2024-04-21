# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two Pointers
        # Initialize two nodes, with lagging pointer (n - 1) nodes behind the pointer ahead.
        # Then move at the same pace until pointer ahead hits the end of the list.
        # Keep track of previous and next node from lagging pointer.
        prev = None
        lag_ptr, ahead_ptr = head, head
        delay = 0
        while ahead_ptr and delay < n:
            ahead_ptr = ahead_ptr.next
            delay += 1

        if not ahead_ptr:
            # reached end of list with delay = sz, must remove the head node
            nxt = lag_ptr.next
            del lag_ptr
            return nxt

        # now lag_ptr is n nodes behind ahead_ptr
        # just need to walk both of them forward together until ahead_ptr hits the end
        while ahead_ptr:
            ahead_ptr = ahead_ptr.next
            prev = lag_ptr
            lag_ptr = lag_ptr.next

        # cut the node at lag_ptr from the list and return the new list
        prev.next = lag_ptr.next
        del lag_ptr
        return head