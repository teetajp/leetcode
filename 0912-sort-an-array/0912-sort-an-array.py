class Solution:
    def mergeSort(self, nums):
        if len(nums) == 1:
            # base case: subarray of len 1, already sorted
            return nums
        
        # divide subarray into two halves (l to m, m+1 to r)
        m = len(nums) // 2
        
        left, right = self.mergeSort(nums[:m]), self.mergeSort(nums[m:])
        
        return self.merge(left, right)
        
    
    def merge(self, left, right) -> List[int]:
        # the two lists are already sorted
        # create a new list by appending the smallest element of the two lists until we run out of elements
        output = []
        l, r = 0, 0
        while l < len(left) or r < len(right):
            if r >= len(right) or (l < len(left) and left[l] <= right[r]):
                output.append(left[l])
                l += 1
            else:
                output.append(right[r])
                r += 1
            
            
        return output
    
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort; repeated divide array into subarrays (base case is when array is of size 1 -> already sorted)
        # in merge step, we are given two subarrays, create a new array of n_1 + n_2 size, and pick smallest to largest to combine
        return self.mergeSort(nums)
        
    