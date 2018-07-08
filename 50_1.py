# inefficient version: O(n)
class Solution:
    def myPow(self,x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1
        if n == 0: return 1
        elif n < 0:
        	for i in range(-n):
        		res = res * 1 / x
        else:
        	for i in range(n):
        		res = res * x
        return res
