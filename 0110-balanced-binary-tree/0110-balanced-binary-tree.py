# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Balanced when difference between left and right subtree is at most 1
        if root is None:
            return True
        
        def getHeight(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            return max(getHeight(root.left), getHeight(root.right)) + 1
        
        return abs(getHeight(root.left) - getHeight(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        