# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # smallest value in a BST is the left most-node
        # 2nd smallest value in a BST is either the leftmost node of the rightsubtree of the 1st smallest OR the parent of the 1st smallest
        # kth smallest value in a BST is the leftmost node of the right subtree of the (k-1)th smallest OR the parent of the previous smallest ones
        
        # do an in order traversal while counting, then return the kth node in order
        self.count = 0
        self.kthSmallest_val = None
        self.in_order_traversal(root, k)
        return self.kthSmallest_val
        
    def in_order_traversal(self, root: Optional[TreeNode], k: int):
        # inorder: left, current, right
        if not root or self.count >= k:
            return
        
        if root.left:
            self.in_order_traversal(root.left, k)
        
        if self.count == k - 1:
            self.kthSmallest_val = root.val
            self.count += 1
            return
        else:
            self.count += 1
        
        if root.right:
            self.in_order_traversal(root.right, k)
            