class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 0
        return self.climbStairs(n-1) + self.climbStairs(n-2) 


"""
Time - 0(2^n)
space - O(1)

"""
