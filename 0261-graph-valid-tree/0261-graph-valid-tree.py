class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """Undirected graph is a valid tree when it has no cycles
        Graph must be connected, otherwise not invalid.
        """
        if n <= 1:
            return True
        
        adjList = defaultdict(set)
        
        if len(edges) != n - 1:
            # n - 1 edges are needed to connect n nodes;
            # there is a cycle if there are n or more edges for n nodes, according to Pigeonhole principle
            return False
        
        while edges:
            src, dest = edges.pop()
            # undirected edges, so add directed edges to and from both nodes
            adjList[src].add(dest)
            adjList[dest].add(src)
        
        if len(adjList) != n:
            # all nodes must have at least one edge
            return False
        
        # nodes that only have one edge are leaf nodes, can disregard
        # nodes that have more than one edge have potential to form cycle, so they are candidates
        
        # run DFS and return False if we encounter other nodes we have seen before
        # also return False if there are still edges at the end of the function
        def DFS(path, cur_idx):
            if cur_idx in path or cur_idx not in adjList:
                return False # cycle exists, not a valid tree
            
            while adjList[cur_idx]:
                neighbor = adjList[cur_idx].pop()
                adjList[neighbor].remove(cur_idx)
                
                path.add(cur_idx)
                
                if not DFS(path, neighbor):
                    return False
                
            del adjList[cur_idx]
            return True
                
            
                
        # check if each node visited once and no nodes/edges remain
        return DFS(set(), 0) and len(adjList) == 0