class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # linked list cycle
        slow, fast = nums[0], nums[nums[0]]
        
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]     
            
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
            
        return slow