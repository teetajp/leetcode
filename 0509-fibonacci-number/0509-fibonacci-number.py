# from collections import deque
class Solution:
    
    def fib(self, n: int) -> int:
        if n == 0: return 0
        fib_memo = [0, 1]
        for i in range(2, n):
            # fib_memo.append(fib_memo[0] + fib_memo[1])
            # fib_memo.popleft()
            fib_memo[0], fib_memo[1] = fib_memo[1], fib_memo[0] + fib_memo[1]
        return fib_memo[0] + fib_memo[1]