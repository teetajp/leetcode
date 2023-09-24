class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # pop elements from the array as you are moving
        x = 0
        for i in nums:
            x ^= i
        return x