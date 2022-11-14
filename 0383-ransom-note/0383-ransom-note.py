from functools import reduce
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = defaultdict(int)
        for c in magazine:
            letters[c] += 1
        for c in ransomNote:
            if letters[c] > 0:
                letters[c] -= 1
            else:
                return False
        return True
