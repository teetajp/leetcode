# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeightBalance(cur: Optional[TreeNode]) -> tuple[bool, int]:
            # returns a tuple (bool, int) with:
            #   the bool representing whether the subtree is balanced
            #   the int representing the height of the subtree
            if not cur:
                return (True, -1)
            elif not cur.left and not cur.right:
                return (True, 0) # no children
            
            isLeftBalanced, leftHeight = getHeightBalance(cur.left)
            isRightBalanced, rightHeight = getHeightBalance(cur.right)
            curHeight = max(leftHeight, rightHeight) + 1
            
            if not (isLeftBalanced and isRightBalanced) or abs(rightHeight - leftHeight) > 1:
                return (False, curHeight) # contains unbalanced subtree
            return (True, curHeight)
        
        return getHeightBalance(root)[0]
            