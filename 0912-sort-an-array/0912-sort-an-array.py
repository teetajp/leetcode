class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort; repeated divide array into subarrays (base case is when array is of size 1 -> already sorted)
        # in merge step, we are given two subarrays, create a new array of n_1 + n_2 size, and pick smallest to largest to combine
        def mergeSort(nums):
            if len(nums) == 1:
                # base case: subarray of len 1, already sorted
                return nums

            # divide subarray into two halves (l to m, m+1 to r)
            m = len(nums) // 2

            left, right = mergeSort(nums[:m]), mergeSort(nums[m:])
            
            merge(left, right, nums)
            
            return nums


        def merge(left, right, output):
            # the two lists are already sorted
            # create a new list by appending the smallest element of the two lists until we run out of elements
            l, r, k = 0, 0, 0
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    output[k] = left[l]
                    l += 1
                else:
                    output[k] = right[r]
                    r += 1
                
                k += 1
            
            output[k:] = left[l:] if l < len(left) else right[r:]


        return mergeSort(nums)
        
    