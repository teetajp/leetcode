from collections import deque
class Solution:
    # @lru_cache(None)
    # def fib(self, n: int) -> int:
    #     if n <= 1: return n
    #     return self.fib(n-1) + self.fib(n-2)
    
    def fib(self, n: int) -> int:
        # fib_memo = [0 for i in range(n+1)]
        # for i in range(2, n+1):
        #     fib_memo.append(fib_memo[i-2] + fib_memo[i-1])
        if n == 0: return 0
        fib_memo = deque([0, 1])
        for i in range(2, n):
            fib_memo.append(fib_memo[0] + fib_memo[1])
            fib_memo.popleft()
        return fib_memo[0] + fib_memo[1]