class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Let CS(i) be the number of distinct ways to climb from the i-th step to the n-th step.
        
        Assume n >= 1
        
        Base Case:
        - CS(n) = 0
        - CS(n-1) = 1
        - CS(n-2) = 2
        - CS(n-3) = 3
        - CS(n-4) = 5 = CS(n-3) + CS(n-2)
        
        Recursive Case:
        - add all distinct ways from climbing 1 or 2 steps
        - CS(i) = CS(i+1) + CS(i+2)
        
        Order:
        - iterate from n down to 0 linearly
        
        Final answer: CS(0)
        """
        cs = [0] * (n+1) # initialize
        if n >= 1:
            cs[n-1] = 1
        if n >= 2:
            cs[n-2] = 2
        
        for i in range(n-3, -1, -1):
            cs[i] = cs[i+1] + cs[i+2]
        
        return cs[0]