import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def node_lt(self, other):
    return self.val <= other.val

ListNode.__lt__ = node_lt

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Since the lists are singly-linked, we need to iterate over each one
        in forward manner while linking them in the head list.
        """
        minHeap = [] # O(k) space
        for idx, node in enumerate(lists):
            # TODO: what if one list is shorter or "None"
            if node:
                # (node.val, idx of linkedlist in list if there is next)
                minHeap.append((node.val, node))
        
        heapq.heapify(minHeap) # O(k)
        
        if not minHeap:
            return None
        
        head = ListNode() # dummy node
        curr = head
        
        while minHeap:
            # append lowest value node to the tail of the linkedlist
            curr.next = minHeap[0][1] # link last node in linkedlist to new node
            curr = curr.next # set current node to tail
            
            # if the node has a next node, add it to the heap
            if curr.next:
                heapq.heapreplace(minHeap, (curr.next.val, curr.next))
            else:
                heapq.heappop(minHeap)
        
        return head.next