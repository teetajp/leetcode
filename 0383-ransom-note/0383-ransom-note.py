class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mletters = Counter(magazine)
        rletters = Counter(ransomNote)
        for k, v in rletters.items():
            if k not in mletters or mletters[k] < v:
                return False
        return True
