class Solution:
    def secondHighest(self, s: str) -> int:
        s = sorted(list(set(int(i) for i in s if i.isnumeric())))
        return s[-2] if len(s) >= 2 else -1