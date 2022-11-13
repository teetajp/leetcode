class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = dict()
        for i in range(len(nums)):
            x = nums[i]
            diff = target - x
            if diff in memo:
                return [i, memo[diff]]
            else:
                memo[x] = i
        return None