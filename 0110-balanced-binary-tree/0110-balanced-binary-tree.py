# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeightBalance(cur: Optional[TreeNode]) -> int:
            if not cur:
                return 0
            
            leftHeight = getHeightBalance(cur.left)
            if leftHeight == -1:
                return -1 # fail early
            
            rightHeight = getHeightBalance(cur.right)
            
            if rightHeight == -1 or abs(rightHeight - leftHeight) > 1:
                return -1
            return 1 + max(leftHeight, rightHeight)
        
        return getHeightBalance(root) != -1
            