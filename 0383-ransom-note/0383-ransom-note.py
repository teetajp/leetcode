class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = Counter(magazine)
        
        for c in ransomNote:
            if letters[c] > 0:
                letters[c] -= 1
            else:
                return False
        return True
