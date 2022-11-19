class Solution:
    def rob(self, nums: List[int]) -> int:
        def simple_rob(start: int, end: int):
            maxLoot = [0, 0] # first index stores the max loot from the i-2th iteration, and second index stores current iteration's max loot
            for i in range(start, end):
                maxLoot[0], maxLoot[1] = maxLoot[1], max(maxLoot[1], nums[i] + maxLoot[0])
            return maxLoot[1]
        if len(nums) == 1: return nums[0]
        return max(simple_rob(0, len(nums)-1), simple_rob(1, len(nums)))