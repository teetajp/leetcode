# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_path_length = 0
        
        def checkLongestPathThrough(middle: Optional[TreeNode]) -> int:
            if not middle:
                return -1 # might need to be -1
            elif not middle.left and not middle.right:
                return 0 # no child nodes
            else:
                left_max = checkLongestPathThrough(middle.left) + 1 # + 1 edge
                right_max = checkLongestPathThrough(middle.right) + 1 # + 1 edge
                nonlocal max_path_length
                max_path_length = max(max_path_length, left_max + right_max)
                return max(left_max, right_max)
        
        checkLongestPathThrough(root)
        return max_path_length