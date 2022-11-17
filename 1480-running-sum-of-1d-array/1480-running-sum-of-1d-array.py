
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return accumulate(nums, lambda x, y: x + y)