# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # two pointers technique, and iterate over both lists together, digit by digit, while adding the sum of each digit to the new linkedlist, and we will keep a variable to store the carry
    # space complexity: O(max(len(l1), len(l2)) + 1) since the new number has either the same number of digits as the larger of the two numbers, or one more digit due to carry-on from addition
    # time complexity: O(max(len(l1), len(l2)) + 1)
   
        sumList = ListNode(val=l1.val + l2.val)
        carry = 0
        head = None
        prev = None
        while l1 and l2:
            # we add the digits together and get the carry by using modulo
            carry, digit = divmod(l1.val + l2.val + carry, 10)
            
            cur = ListNode(val=digit)
            
            if head is None and prev is None:
                head = cur
                prev = cur
            else:            
                prev.next = cur
                prev = cur
                
            l1, l2 = l1.next, l2.next
        
        # handle case one of the lists is shorter
        l3 = l1 or l2
        
        
        while l3 is not None and carry == 1:
            carry, digit = divmod(l3.val + carry, 10)
            cur = ListNode(val=digit)
                     
            prev.next = cur
            prev = cur
            l3 = l3.next
        
        else:
            if l3 is None and carry == 1:
                prev.next = ListNode(val=carry)
            else:
                prev.next = l3    
        
        return head
   