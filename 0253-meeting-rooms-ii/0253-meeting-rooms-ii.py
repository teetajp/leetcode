class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # find the maximum number of overlapping intervals at one time
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        res = 0
        meetings = [] # heap sorted on meeting end times
        
        for curStart, curEnd in intervals:
            while meetings and meetings[0] <= curStart:
                heapq.heappop(meetings)
            heapq.heappush(meetings, curEnd)
            res = max(res, len(meetings))
            
        return res