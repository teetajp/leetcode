# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Want to traverse all branches of the tree and append the rightmost node at each depth
        """
        res = []
        def rightSideViewRec(cur: Optional[TreeNode], depth: int) -> None:
            if not cur:
                return
            elif len(res) == depth:
                # first time reaching this depth, so we must be in the rightmost node at this depth
                res.append(cur.val)
            
            # traverse right child first so we add the rightmost node first
            rightSideViewRec(cur.right, depth + 1)
            rightSideViewRec(cur.left, depth + 1)
            
        rightSideViewRec(root, 0)
        
        return res