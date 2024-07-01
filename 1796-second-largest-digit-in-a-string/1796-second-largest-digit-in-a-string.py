class Solution:
    def secondHighest(self, s: str) -> int:
        s = list(set(-int(i) for i in s if i.isnumeric()))
        heapq.heapify(s)
        if s:
            heapq.heappop(s)
        return -heapq.heappop(s) if s else -1