# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (not head) or (not head.next) or k == 1:
            return head
        
        """Since we are not sure when the list will end and whether there will be a list of nodes at the end that is not a multiple of k, we need to either traverse through the whole list of nodes and count them all first, or we need to traverse each k nodes at a time then reverse them (same time complexity)."""
        sublist_len = 1
        curr = head
        first_new_head = None
        prev_sublist_tail = None
        
        while curr:
            # Reverse prefix sublist of len k from current pos when possible
            if sublist_len % k == 1:
                # start a new sublist
                original_sublist_head = curr # will be reversed_sublist_tail
            elif sublist_len % k == 0:
                original_sublist_tail = curr
                next_sublist_head = curr.next # track next node before reverse
                
                self.reverseList(original_sublist_head, original_sublist_tail)
                new_head, new_tail = original_sublist_tail, original_sublist_head
                
                if not first_new_head: # new head of the entire list
                    first_new_head = new_head
                
                # link previous reversed sublist tail with new reversed head
                if prev_sublist_tail:
                    prev_sublist_tail.next = new_head
                    
                 # connect new tail to next (unreversed) sublist
                new_tail.next = next_sublist_head
                
                prev_sublist_tail = new_tail
                curr = new_tail
            
            # increment / traverse list
            sublist_len += 1
            curr = curr.next
            
        # Case when last sublist is not a multiple of k: already handled (noOp)
            
        return first_new_head
        
        
    def reverseList(self, curr, tail, prev=None) -> Optional[ListNode]:
        nxt = curr.next
        curr.next = prev
        
        if curr != tail:
            self.reverseList(nxt, tail, curr)
        