class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological Sort with BFS
        
        prereqMap = defaultdict(list)
        
        for crs_idx, pre_idx in prerequisites:
            prereqMap[crs_idx].append(pre_idx)
            
        ordering = []
        visited = set() # courses we have added to ordering
        self.hasCycle = False
        
        def DFS(visited, path, crs):
            if crs in visited:
                # already added to ordering, so ignore
                return
            if crs in path:
                # course is in current chain of prereqs
                raise Exception("Cycle Detected")
                
            path.add(crs)
            while prereqMap[crs]:
                prereq = prereqMap[crs].pop()
                DFS(visited, path, prereq)
                
            path.remove(crs)
            ordering.append(crs)
            visited.add(crs)
        
        try:
            for crs in range(numCourses):
                DFS(visited, set(), crs)
        except: # cycle detected
            return [] 
        
        return ordering