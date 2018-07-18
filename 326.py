class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 3**19 = 1162261467
        # 3**20 = 3486784401
        # INT_MAX = 2147483647
        if n <= 0: return False
        else:
            return 1162261467 % n == 0