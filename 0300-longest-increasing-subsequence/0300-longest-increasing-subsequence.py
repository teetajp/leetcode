from sortedcontainers import SortedList

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_lens = SortedList()
        for i in range(len(nums)):
            p = max_lens.bisect_right((nums[i], 0))
            l = 1 if p == 0 else max_lens[p-1][1] + 1
            while p < len(max_lens) and max_lens[p][1] <= l:
                max_lens.pop(p)
            max_lens.add((nums[i], l))
        return max_lens[-1][1]