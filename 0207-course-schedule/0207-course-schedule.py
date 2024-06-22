class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if there is a cycle, then can't finish
        # if no cycle, then true
        # ==> graph must be a DAG
        # ==> topSort then DFS?
        
        # each node should not be able to reach itself
        prereqs = defaultdict(set)
        
        for course, prereq_course in prerequisites:
            prereqs[course].add(prereq_course)
        
        has_searched = set()
        
        def has_cycle(visited, course_idx):
            if course_idx in has_searched:
                return False
            if course_idx in visited:
                return True
            
            visited.add(course_idx)
            
            for prereq_idx in prereqs[course_idx]:
                if has_cycle(visited, prereq_idx):
                    return True
                
            visited.remove(course_idx)
            has_searched.add(course_idx)
            return False
        
        return not any(has_cycle(set(), i) for i in range(numCourses))