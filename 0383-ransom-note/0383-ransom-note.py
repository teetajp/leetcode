class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ml = Counter(magazine)
        rl = Counter(ransomNote)
        for k, v in rl.items():
            if k not in ml or ml[k] < v:
                return False
        return True
