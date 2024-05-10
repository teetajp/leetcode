from collections import defaultdict
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # first, deep copy the nodes in order
        # while iterating through the original node list,
        # keep a list of (copied.random, original_node) in sorted order
        
        # When we assign the random pointers, we only want to iterate through
        # the original list once, so we need to keep those pairs in sorted order
        
        # when we see a non-null random ptr, add it to a dict
        # with the key being the destination node, value being list of node ptrs that need to be assigned
        
        # handle case when n = 0
        if head is None:
            return None
        
        random_dests = defaultdict(list)
        head_cpy = Node(head.val)
        # node_by_id = {id(head): head_cpy} # key: node id, value: node in copied list
        
        og_cur = head
        cp_cur = head_cpy
        
        while og_cur:
            cp_cur.next = Node(og_cur.next.val) if og_cur.next else None
            
            if og_cur.random:
                random_dests[id(og_cur.random)].append(cp_cur)
            
            og_cur = og_cur.next
            cp_cur = cp_cur.next
        
        og_cur, cp_cur = head, head_cpy
        
        while og_cur and cp_cur:
        # lookup current node to see if it is pointer to by any random ptrs
            for cp_parent_src in random_dests[id(og_cur)]:
                cp_parent_src.random = cp_cur
                
            og_cur, cp_cur = og_cur.next, cp_cur.next
            
        return head_cpy