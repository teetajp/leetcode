class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # we want to find any index where the jump[i] >= (n-1)
        # to get to that index, we need to find an index j where jump[j] >= i
        # and so on...
        # could go through the array to find an index where jump[i] >= n-1
        # as we are going through, we keep an another array of booleans representing whethere a jump is reachable, then update it
        if len(nums) == 0: return True
        max_index = nums[0]
        curr_i = 1
        while curr_i <= max_index and curr_i < len(nums)-1 and max_index < len(nums)-1:
            max_index = max(max_index, curr_i + nums[curr_i])
            curr_i += 1
        return max_index >= len(nums) - 1