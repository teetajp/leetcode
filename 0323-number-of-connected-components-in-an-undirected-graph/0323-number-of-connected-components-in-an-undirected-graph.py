class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """Union-find algorithm to count number of disjoint sets / connected components"""
        parent = [i for i in range(n)]
        rank = [1] * n
        
        def find(node):
            """Find the parent of the set"""
            while node != parent[node]:
                parent[node] = parent[parent[node]] # compress path; XXX: what about rank?
                node = parent[node]
            return node
            
        def union(node1, node2):
            """Merge two sets together if possible"""
            parent1, parent2 = find(node1), find(node2)
            
            if parent1 == parent2:
                return # same parent, do nothing
            
            # union by rank
            if rank[parent1] >= rank[parent2]:
                rank[parent1] += rank[parent2]
                parent[parent2] = parent1
            else:
                rank[parent2] += rank[parent1]
                parent[parent1] = parent2
            
            
        
        for a, b in edges:
            union(a, b)
        
        # count the number of connected components by checking for nodes with no outgoing edge
        return sum(parent[i] == i for i in range(n))