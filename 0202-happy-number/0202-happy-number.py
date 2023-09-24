class Solution:
    def isHappy(self, n: int) -> bool:
        numDigits = n // 10
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            sum_square = 0
            while n != 0:
                sum_square += (n % 10) ** 2
                n //= 10
            n = sum_square
            
        return n == 1
            
            
            