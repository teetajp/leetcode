# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        """
        maxDist is simplify the distance between the first and last distinct critical point
        
        minDist can be found by comparing/updating the current min against the distance between each new crit point and the prev one.
        """
        firstIdx = lastIdx = minDist = None
        curIdx = 1
        
        prev, cur = head, head.next
        
        while cur.next:
            
            if prev.val < cur.val > cur.next.val or prev.val > cur.val < cur.next.val:
                # current node is a critical point
                if not firstIdx:
                    firstIdx = curIdx
                elif lastIdx:
                    minDist = min(minDist, curIdx - lastIdx) if minDist else curIdx - lastIdx
                    
                lastIdx = curIdx
            
            prev, cur = cur, cur.next
            curIdx += 1
        
        
        
        
        return [minDist if minDist else -1, lastIdx - firstIdx if firstIdx != lastIdx else -1]