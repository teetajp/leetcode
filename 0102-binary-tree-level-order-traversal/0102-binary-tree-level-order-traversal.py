# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        
        q = Deque([root])
        res = []
        
        while q:
            levelNodes = []
            size = len(q)
            
            for i in range(size):
                cur = q.popleft()
                levelNodes.append(cur.val)
                if cur.left is not None:                
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            
            res.append(levelNodes)
        
        return res