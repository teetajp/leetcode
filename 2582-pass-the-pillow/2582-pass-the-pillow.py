class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # takes n-1 passes to reach one end from the other
        
        if (time // (n-1)) % 2 == 0: # even number of rounds
            # => current direction is left-to-right
            return (time % (n-1)) + 1
        else: # odd number of rounds
            # => current direction is right-to-left
            return n - (time % (n-1))