# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Pre-order traversal: cur, left, right
        In-order traversal: left, cur, right
        
        Properties:
        - First node in preorder traversal is always root
        - Rightmost val is always the same for pre-order and in-order traversal.
        - While we may not be able to tell if the next node in the preorder traversal is the left or right child (since cur node may not have both child), given that all node values are unique, we can use the in-order traversal to determine whether the next val is the preorder traversal's left child if the next val in the in-order traversal also matches.
        - Need to locate the current node val in the inorder traversal, anything on left is on left subtree, anything on right is on right subtree.
        """
        p_idx = 0
        
        def buildTreeRec(subtree_start, subtree_end):
            nonlocal p_idx
            if p_idx >= len(preorder) or subtree_start >= subtree_end:
                return None
            
            root_val = preorder[p_idx]
            root_idx = None
            for i in range(subtree_start, subtree_end):
                if inorder[i] == root_val:
                    root_idx = i
                    break
            else:
                return None
            
            subtree_root = TreeNode(root_val)
            p_idx += 1
            
            subtree_root.left = buildTreeRec(subtree_start, root_idx)
            subtree_root.right = buildTreeRec(root_idx + 1, subtree_end)
            return subtree_root
        
        return buildTreeRec(0, len(inorder))