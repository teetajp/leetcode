class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if there is a cycle, then can't finish
        # if no cycle, then true
        # ==> graph must be a DAG
        # ==> topSort then DFS?
        
        # each node should not be able to reach itself
        prereqs = defaultdict(list)
        
        for course, prereq_course in prerequisites:
            prereqs[course].append(prereq_course)
        
        has_searched = [False] * numCourses
        remaining = numCourses
        
        def has_cycle(visited, course_idx):
            if has_searched[course_idx]:
                return False
            if course_idx in visited:
                return True
            if len(prereqs[course_idx]) == 0:
                return False
            
            visited.add(course_idx)
            
            while prereqs[course_idx]:
                prereq_idx = prereqs[course_idx].pop()
                if has_cycle(visited, prereq_idx):
                    return True
                
            visited.remove(course_idx)
            has_searched[course_idx] = True
            nonlocal remaining
            remaining -= 1
            return False
        
        for i in range(numCourses):
            if (not has_searched[i]) and has_cycle(set(), i):
                return False
            if remaining == 0:
                return True
            
        return True