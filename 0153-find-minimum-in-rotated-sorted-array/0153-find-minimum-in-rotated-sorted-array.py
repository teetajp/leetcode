class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find the first point where nums[i-1] > nums[i] and return nums[i]
        # if rotated n times, then nums[0] < nums[i] for 1 <= i < n
        # if rotated n-1 times, then nums[n-1] < nums[i] for 0 <= i < n-1
        l, r = 0, len(nums) - 1
        
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            
            # else nums[l] > nums[r] (all elems are unique)
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
                
                
        
        return nums[r]