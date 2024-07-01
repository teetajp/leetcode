class Solution:
    def secondHighest(self, s: str) -> int:
        s = list(set(int(i) for i in s if i.isnumeric()))
        return sorted(s)[-2] if len(s) >= 2 else -1