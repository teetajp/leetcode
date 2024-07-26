class Solution:
    @functools.cache
    def myPow(self, x: float, n: int) -> float:
        """
        -100.0 < x < 100.0
        but -2^31 <= n <= 2^31 - 1
        so the exponent can be very big and dominates the running time
        """
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        
        return (x if n % 2 == 1 else 1) * self.myPow(x, n // 2) * self.myPow(x, n // 2)