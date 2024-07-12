# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        """
        New head is the first node in the list that doesn't have a duplicate
        
        Otherwise return None
        """
        
        val_counts = {}
        cur = head
        
        while cur:
            val_counts[cur.val] = val_counts.get(cur.val, 0) + 1
            cur = cur.next
        
        cur = head
        head = ListNode(val=0) # dummy node
        prev_valid = head
        
        while cur:
            if val_counts[cur.val] == 1:
                prev_valid.next = cur
                prev_valid = cur
                
            cur = cur.next
            
        prev_valid.next = None
                
        return head.next