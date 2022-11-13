class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = defaultdict(int)
        for char in s:
            counts[char] += 1
        for char in t:
            if counts[char] == 0:
                return False
            counts[char] -= 1
        return True