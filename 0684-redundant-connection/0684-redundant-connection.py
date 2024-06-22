class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Brute force: DFS after every insert to determine if number of nodes in CC remained the same --> O(n^2) time, O(n) space
        Efficient: Union-find after every insert to see if the two endpoints are already connected before insertion --> O(n*invAck(n)) time, O(n) space
        
        """
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1] * (n+1)
        
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]] # path compression
                node = parent[node]
            return node
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            
            if p1 == p2:
                # nodes are already connected
                return [node1, node2]
            
            # union by rank
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            elif rank[p1] > rank[p2]:
                parent[p2] = p1
            else:
                # equal rank
                parent[p2] = p1
                rank[p1] += 1
            
        res = None    
        for a, b in edges:
            res = union(a, b) or res
                
        return res