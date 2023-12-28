# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # we are guaranteed that the BST has nodes p and q, and the BST has at least two nodes
        # so at the very least, the root is a common ancestor (but not necessarily the lowest)
        
        # if we take the prefix of the path for p and q, respectively.
        #   Then, the LCA is the last node the prefix paths had in common with each other, possibly being p or q.
        self.p, self.q = p, q
        self.path_p, self.path_q = None, None
        self.prefix = []
        
        self.DFS(root)
            
        # the lowest common ancestor is a single node, so its either a strict ancestor of both p and q, or its one of p or q itself
        # so, this lowest common ancestor is on both p and q's prefix path where it has equal length
        while self.path_p[-1] != self.path_q[-1]:
            
            if len(self.path_p) >= len(self.path_q):
                self.path_p.pop()
            else:
                self.path_q.pop()

        return self.path_p[-1]
                
        
    def DFS(self, cur: 'TreeNode'):
        if cur is None or self.path_p and self.path_q:
            return
        
        self.prefix.append(cur)
        
        # check current node against p and q
        if not self.path_p and cur == self.p:
            self.path_p = self.prefix.copy()
        elif not self.path_q and cur == self.q:
            self.path_q = self.prefix.copy()
        
        # check children nodes
        self.DFS(cur.left)
        self.DFS(cur.right)
        
        self.prefix.pop()