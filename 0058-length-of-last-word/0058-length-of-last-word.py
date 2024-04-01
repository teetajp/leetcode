class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start = end = len(s)
        for i in reversed(range(len(s))):
            if s[i] != ' ':
                start = i
                continue
            # char is space
            if start < end:
                break
            end = i
            
            
        return end - start