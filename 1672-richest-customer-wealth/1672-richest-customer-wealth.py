class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(lambda banks: sum(banks), accounts))