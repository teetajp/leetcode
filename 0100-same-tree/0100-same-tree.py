# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif (not p or not q) or (p.val != q.val):
            return False
        # p and q have the same value
        
        # check children nodes
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    # Time Complexity: O(n) where n is the total number of nodes (# in p + # in q)
    # Space Complexity: O(log n) = O(h), aka the min height between p and q
        