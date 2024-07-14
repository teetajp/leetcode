# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Cases:
            single node: that node
            root with left XOR right child: root only, child only, or child + root
            root with left AND right child: root only, left only, right only, left + root, root + right, left + root + right
            
            If include root and a child, then child's subtree cannot have a split.
            
            return to parent: sum of straight path (no split)
            global res: at each node, check sum including itself (root) and left and/or right, BUT return max sum of straight path including root
        """
        globalRes = root.val
        
        def maxPathSumRec(subroot: Optional[TreeNode]) -> int:
            """Returns the maximum path sum through the given node with no split.
            Updates the global max with max path sum considering split.
            """
            if not subroot:
                return float("-inf")
            
            leftRes, rightRes = maxPathSumRec(subroot.left), maxPathSumRec(subroot.right)
            
            maxSumThroughSubroot = max(subroot.val, subroot.val + leftRes, subroot.val + rightRes)
            
            nonlocal globalRes
            globalRes = max(globalRes, maxSumThroughSubroot, subroot.val + leftRes + rightRes)
            
            
            return max(subroot.val, subroot.val + leftRes, subroot.val + rightRes)
        
        maxPathSumRec(root)
        return globalRes