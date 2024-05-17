# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBSTrec(cur: Optional[TreeNode],
                         minVal=float('-inf'), maxVal=float('inf')) -> bool:
            if not cur:
                return True
            
            res = (minVal < cur.val < maxVal)
            res &= isValidBSTrec(cur.left, minVal, cur.val)
            res &= isValidBSTrec(cur.right, cur.val, maxVal)
            return res
        
        return isValidBSTrec(root)