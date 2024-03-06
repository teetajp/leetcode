# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    # print current, then right, then left
    # BFS
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # need to go through all level and pick the right-most node (could be "left" brach of parent)
        levels = []
        # BFS
        queue = deque([(root, 0)])
        while queue:
            node, level_idx = queue.pop()
            if node is None:
                continue
            if len(levels) == level_idx:
                # first node we see from the right side (if we go to node on the right first)
                levels.append(node.val)
            queue.appendleft((node.right, level_idx + 1)) # important to put this first
            queue.appendleft((node.left, level_idx + 1))

        return levels