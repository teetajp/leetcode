class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological Sort
        # we want to take courses with no prereqs first then the ones with those earlier prereqs
        
        # build adjacency list
        
        prereqMap = defaultdict(list) # key: course_idx, value: indices of courses that key is prereq to
        eligible_crs = set(i for i in range(numCourses)) # set of courses with no prereqs (or prereqs have been fulfilled)
        prereqsNeeded = {}
        
        for course, prereq in prerequisites:
            prereqMap[prereq].append(course)
            eligible_crs.discard(course)
            prereqsNeeded[course] = prereqsNeeded.get(course, 0) + 1
            
        
        if not eligible_crs:
            return []
        
        ordering = []
        while eligible_crs:
            crs = eligible_crs.pop()
            ordering.append(crs)
            
            while prereqMap[crs]:
                sequel_crs = prereqMap[crs].pop()
                prereqsNeeded[sequel_crs] -= 1
                
                if prereqsNeeded[sequel_crs] == 0:
                    del prereqsNeeded[sequel_crs]
                    eligible_crs.add(sequel_crs)
        
        return ordering if len(prereqsNeeded) == 0 else []