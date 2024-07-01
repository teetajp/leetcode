class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        """
        Person a if acquainted with person b if person a is directly friends with person b, or has an indirect (non-first degree) connection with person b.
        
        Edges are undirected, so apply edges to both sides.
        Being acquainted means reachable through some connection with DFS.
        Must be at least n-1 edges to form a connected component.
        
        Want to find earliest timestamp in which the graph forms a single connected component.
        
        Algo:
        - sort log (edges) by timestamp via sorting algo or heap
        - construct union find, run merge on each edge until fully run out of edges or only have one CC.
        """
        if len(logs) < n - 1:
            return -1 # not enough connections for everyone to become friends, by the Pigeonhole principle
        
        # each individual forms their own singleton group, initially
        parent = [i for i in range(n)]
        rank = [0] * n
        num_groups = n
        
        ### Union-Find/Disjoint-set data structure
        def find(idx):
            """Find index of parent/root node"""
            if idx != parent[idx]:
                # this node is not a root of the disjoint set
                # traverse up to parent node while performing path compression
                parent[idx] = find(parent[idx])
            
            return parent[idx]
        
        def union(person1, person2):
            """
            Connects two person and their groups together if not already connected
            
            :Returns True on success, False if groups already connected
            """
            src1, src2 = find(person1), find(person2)
            
            if src1 == src2:
                return False # both node already in same disjoint-set
            
            # union by rank
            if rank[src1] < rank[src2]:
                parent[src1] = parent[src2]
            elif rank[src1] > rank[src2]:
                parent[src2] = parent[src1]
            else:
                parent[src2] = parent[src1]
                rank[src1] += 1
            
            return True
        ###
        
        logs.sort(reverse=True)
        
        while logs and num_groups > 1:
            timestamp, person_a, person_b = logs.pop()
            
            if union(person_a, person_b):
                num_groups -= 1
        
        # return most recent timestamp when graph became connected, else -1
        return timestamp if num_groups == 1 else -1