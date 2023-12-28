class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        # l == r
        k, n = l, len(nums) # k is the number of rotations, also the index of the pivot
        l, r = 0, n - 1
        
        while l <= r:
            mid = l + (r - l) // 2 # "middle of the array, before rotations"
            rotated_mid = (mid + k) % n # index of the middle of the array, after rotations
            
            if target == nums[rotated_mid]:
                return rotated_mid
            elif target < nums[rotated_mid]:
                r = mid - 1
            else:
                l = mid + 1
                
        return -1