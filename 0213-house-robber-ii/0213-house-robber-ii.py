class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache
        def maxLoot(i: int, end: int, willRob: bool) -> int:
            # end is exclusive
            if i >= end:
                return 0
            if willRob:
                return nums[i] + maxLoot(i+2, end, False)
            return max( maxLoot(i, end, True), maxLoot(i+1, end, True) )
        res = max( maxLoot(0, n-1, True), nums[n-1] + maxLoot(1, n-2, False))
        if n >= 2:
            res = max(res, maxLoot(1, n, True), nums[n-2] + maxLoot(0, n-3, False))
        return res
               
        # Case 1: Rob 0th house, can't rob n-1th house, can't rob 1st house
               # Check nums[2...n-1]
        # Case 2: Rob n-1th house, can't rob 0th house, can't rob n-2th house
               # Check nums[1...n-2]
        # Case 3: Rob 1st house: can't rob 0th house or 2nd house
               # Check nums[3...n]
        # Case 4: Rob n-2th house, can't rob n-1th house, can't rob n-3th house
               # Check nums[0...n-4]