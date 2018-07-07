# Eficient version: O(log2(n))
# (reference) http://d.hatena.ne.jp/kazu-yamamoto/20090223/1235372875
import sys
sys.setrecursionlimit(100000)
class Solution:
    def myPow(self,x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = -n
            x = 1 / x
        if n == 0: return 1
        elif n % 2 == 0: return self.myPow(x*x, n/2)
        else: return x * self.myPow(x,n-1)