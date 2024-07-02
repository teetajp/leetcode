class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = Counter(nums1), Counter(nums2)
        res = []
        for k in nums1.keys() & nums2.keys():
            for _ in range(min(nums1[k], nums2[k])):
                res.append(k)
        
        return res