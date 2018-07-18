class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 4**15 = 1073741824
        # 4**16 = 4294967296
        # INT_MAX = 2147483647
        if num <= 0: return False
        else:
            return num in [4**nums for nums in range(16)]