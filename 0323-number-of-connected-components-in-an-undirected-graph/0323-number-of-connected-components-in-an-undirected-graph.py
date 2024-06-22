class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """Run DFS on every node since there could be more than 1 connected component.
        - Need a way to keep track of number of connected components and visited nodes.
        - Some nodes may not have edges and are considered a separate connected component
        XXX: How to check for distinct CC?
        XXX: Need to watch out for cycles
        - can do union find or DFS
        """
        
        adjList = defaultdict(list) 
    
        for nodeA, nodeB in edges:                
            adjList[nodeA].append(nodeB)
            adjList[nodeB].append(nodeA)
        
        numComponents = n - len(adjList) # number of single-node connected components (that has no edges)
        
        def deleteNodesDFS(node):
            while adjList[node]:
                neighbor = adjList[node].pop()
                deleteNodesDFS(neighbor)
            del adjList[node]
            
        for node in range(n):
            if node in adjList:
                numComponents += 1
                deleteNodesDFS(node)
        
        return numComponents
    
    
    # runtime: O(E + V)
    # space: O(E + V)