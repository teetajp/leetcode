class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum == 0:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    r -= 1
                
                while l < r and l > i + 1 and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and r < len(nums) - 1 and nums[r] == nums[r + 1]:
                    r -= 1

        return triplets
            