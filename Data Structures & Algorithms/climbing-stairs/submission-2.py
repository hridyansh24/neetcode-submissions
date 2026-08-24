class Solution:
    def climbStairs(self, n: int) -> int:

        def recf(i):
            if i>=n:
                return i==n
            return recf(i+1) + recf(i+2)
        
        return recf(0)
        