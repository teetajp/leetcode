class Solution: 
    def fib(self, n: int) -> int:
        fib_memo = [0, 1]
        for i in range(2, n):
            fib_memo[0], fib_memo[1] = fib_memo[1], fib_memo[0] + fib_memo[1]
        return fib_memo[0] + fib_memo[1] if n > 1 else fib_memo[n]