class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # need carry bits
        # look for number that does not end in 9 - set previous digits to 0
        
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                # need to carry
                return digits
        return [1] + digits # append new leading 1 to the digits