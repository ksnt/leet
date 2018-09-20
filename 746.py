class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f_1 = 0
        f_2 = 0
        for c in reversed(cost):
            f_1, f_2 = c  + min(f_1,f_2), f_1
        return min(f_1,f_2)