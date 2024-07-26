class Solution:
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
        
        if n % 2 == 1:
            # odd
            return x * self.myPow(x * x, n // 2)
        else:
            return self.myPow(x * x, n // 2)