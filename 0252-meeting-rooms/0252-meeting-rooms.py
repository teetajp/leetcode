class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # check whether all meetings are disjoint
        intervals.sort(key=lambda x: (x[0], x[1]))
        
        for i, intv in enumerate(intervals[:-1]):
            if intv[1] > intervals[i+1][0]:
                return False
        
        return True