class Solution:
    def climbStairs(self,n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        first = 1
        second = 2
        for i in range(2,n):
            third = first + second
            first  = second
            second = third
        return second