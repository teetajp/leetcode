# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    DFS with max value in prefix (path) comparison
    """ 
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 # empty tree, no nodes
        
        self.prefix_max = root.val
        self.count_good_nodes = 0
        
        def goodNodesRec(cur: TreeNode) -> None:
            if not cur:
                return
            
            if self.prefix_max <= cur.val:
                # current node is a good node
                self.count_good_nodes += 1
            
            # remember path's max from root up to this node for backtracking
            parent_prefix_max = self.prefix_max
            
            # update prefix_max before recursing
            self.prefix_max = max(self.prefix_max, cur.val)
            goodNodesRec(cur.left)
            goodNodesRec(cur.right)
            
            # backtrack
            self.prefix_max = parent_prefix_max
            return
            
        goodNodesRec(root) # start from root (root is always good node)
        return self.count_good_nodes
        