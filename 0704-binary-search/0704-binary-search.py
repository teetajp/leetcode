class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(lb, ub):
            if ub - lb <= 1:
                if nums[ub] == target:
                    return ub
                elif nums[lb] == target:
                    return lb
                else:
                    return -1
            mid = (ub + lb) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return binarySearch(mid, ub)
            elif target < nums[mid]:
                return binarySearch(lb, mid)
        return binarySearch(0, len(nums)-1)