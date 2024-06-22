"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        def cloneNode(orgNode: Optional['Node'], clonedNodes: dict[int, 'Node']):
            if not orgNode:
                return orgNode
            elif orgNode.val in clonedNodes:
                # copy of the given node exists
                return clonedNodes[orgNode.val]
            
            # node doesn't exist, create it
            copyNode = Node(orgNode.val)
            clonedNodes[orgNode.val] = copyNode # add cur node to clone graph
            
            # add cloned neighbors by recursing on them
            for orgNeighbor in orgNode.neighbors:
                clonedNeighbor = clonedNodes.get(orgNeighbor.val, None) or \
                                 cloneNode(orgNeighbor, clonedNodes)
                # TODO: check clone graph instead
                copyNode.neighbors.append(clonedNeighbor)
            
            return copyNode
        
        
        return cloneNode(node, {})