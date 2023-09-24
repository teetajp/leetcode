class Solution:
    def hammingWeight(self, n: int) -> int:
        
        return sum( int(digit) for digit in format(n, 'b') )