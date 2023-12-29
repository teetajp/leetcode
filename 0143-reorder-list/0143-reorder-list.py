# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle node
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            
        # slow pointer will be the middle in odd cases, and last of first list in even cases
        
        # reverse second half of the list
        prev, cur = None, slow.next
        while cur:
            nxt = cur.next
            prev, cur.next = cur, prev
            cur = nxt
        
        # prev is now the head of second, reversed list
        
        slow.next = None # cut off the first half from the second half of the list, since they are now reversed
        
        # merge the two lists together
        head1, head2 = head, prev
        while head1 and head2:
            head1_nxt, head2_nxt = head1.next, head2.next
            
            head1.next = head2
            head1 = head1_nxt
            
            head2.next = head1
            head2 = head2_nxt
            
            
        return head