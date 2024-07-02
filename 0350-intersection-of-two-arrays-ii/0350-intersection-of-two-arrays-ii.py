class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = Counter(nums1), Counter(nums2)
        res = []
        for k in set(nums1.keys()).intersection(set(nums2.keys())):
            res.extend([k] * min(nums1[k], nums2[k]))
        
        return res