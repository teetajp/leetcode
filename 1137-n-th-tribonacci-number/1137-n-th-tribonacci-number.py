class Solution:
    def tribonacci(self, n: int) -> int:
        T = [0, 1, 1]
        for i in range(3, n):
            T[0], T[1], T[2] = T[1], T[2], T[0] + T[1] + T[2]
        return T[0] + T[1] + T[2] if n > 2 else T[n]
        