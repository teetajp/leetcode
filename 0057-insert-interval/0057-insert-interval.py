class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, start, end = 0, 0, 1
        merged = []
        
        while i < len(intervals) and intervals[i][1] < newInterval[0]: # interval in list does not overlap with new interval (end < new_start)
            merged.append(intervals[i])
            i += 1
        
        # merge all intervals that overlap with newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        merged.append(newInterval)
        
        # add remaining intervals
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        
        return merged