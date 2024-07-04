# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            Upon encountering a node with val 0,
            set prev (zero) node val to the accumulated sum, reset the sum to 0. Recurse into next node.
            
            When current node is not 0 val, delete current node and set prev pointer to next.
            Recurse into next node but with the deleted node's value added to the sum.
            
            When reach the end, delete the last 0.
        """
        prev, cur, acc = head, head.next, 0
        while True:
            if cur.val == 0:
                prev.val = acc
                
                # recurse except for last zero node
                if cur.next:
                    prev, cur, acc = cur, cur.next, 0
                else:
                    prev.next = None
                    return head
                
            else:
                prev.next = cur.next
                cur, acc = cur.next, acc + cur.val
            
                      
    
    
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         def mergeNodesRec(prev: ListNode, cur: Optional[ListNode], acc: int):
#             """
#             Upon encountering a node with val 0,
#             set prev (zero) node val to the accumulated sum, reset the sum to 0. Recurse into next node.
            
#             When current node is not 0 val, delete current node and set prev pointer to next.
#             Recurse into next node but with the deleted node's value added to the sum.
            
#             When reach the end, delete the last 0.
#             """
            
#             if cur.val == 0:
#                 prev.val = acc
                
#                 # recurse except for last zero node
#                 if not cur.next:
#                     prev.next = None
#                 else:
#                     mergeNodesRec(cur, cur.next, 0)
#             else:
#                 prev.next = cur.next
#                 mergeNodesRec(prev, cur.next, acc + cur.val)
            
                      
        
#         mergeNodesRec(head, head.next, 0)
#         return head