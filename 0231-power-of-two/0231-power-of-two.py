import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return math.log2(n) % 1 == 0 if n > 0 else False   