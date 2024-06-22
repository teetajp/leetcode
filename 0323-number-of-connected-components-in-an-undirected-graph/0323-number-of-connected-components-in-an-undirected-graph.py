class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """Run DFS on every node since there could be more than 1 connected component.
        - Need a way to keep track of number of connected components and visited nodes.
        - Some nodes may not have edges and are considered a separate connected component
        XXX: How to check for distinct CC?
        XXX: Need to watch out for cycles
        - can do union find or DFS
        """
        
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        for a, b in edges:
            union(a, b)

        # Count the number of unique roots
        numComponents = len(set(find(i) for i in range(n)))
        
        return numComponents

    
    # runtime: O(E + V)
    # space: O(E + V)