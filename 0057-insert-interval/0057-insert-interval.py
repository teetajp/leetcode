class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # iterate over intervals to find the right spot (can use binary search)
        # if new_int.end < cur_int.start:
        #       insert
        # if cur_int.start < new_int.start and cur_int.end < new_int.start:
        #       able to insert after, but check next
        #       - ignore this case because going in ascending order and the previous case covers it
        # if cur_int.start <= new_int.start and cur_int.end >= new_int.start:
        #       overlap, insert
        # if end of intervals:
        #       insert
        # if new_int.start <= cur_int.start and new_int.end >= cur_int.start:
        #       overlap, insert
        #
        # iterate over the array, merging as necessary
        #    cur_int.start = min(cur_int.start, new_int.start)
        #    cur_int.end = max(cur_int.end, new_int.end)
        for i, cur_int in enumerate(intervals):
            if newInterval[1] < cur_int[0]:
                intervals.insert(i, newInterval)
                return intervals
            elif (cur_int[0] <= newInterval[0] and cur_int[1] >= newInterval[0]) or (newInterval[0] <= cur_int[0] and newInterval[1] >= cur_int[0]):
                # overlap, insert and merge
                cur_int[0] = min(cur_int[0], newInterval[0])
                cur_int[1] = max(cur_int[1], newInterval[1])
                newInterval = None
                break
            
        if newInterval is not None: # have not inserted
            intervals.append(newInterval) # might need to deep copy
        
        if len(intervals) < 2:
            return intervals
        
        # merge intervals
        mergedIntervals = []
        mergedIntervals.append(intervals[0])
        for i in range(1, len(intervals)):
            if (mergedIntervals[-1][0] <= intervals[i][0] and mergedIntervals[-1][1] >= intervals[i][0]) or \
                (intervals[i][0] <= mergedIntervals[-1][0] and intervals[i][1] >= mergedIntervals[-1][0]):
                    mergedIntervals[-1][0] = min(mergedIntervals[-1][0], intervals[i][0])
                    mergedIntervals[-1][1] = max(mergedIntervals[-1][1], intervals[i][1])
            else:
                mergedIntervals.append(intervals[i])
        
        return mergedIntervals
            
        
        