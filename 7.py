import functools
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_rev_str = []
        x_str = str(x)
        x_str = x_str[::-1] # reverse
        for s in x_str:
        	if s == '-': x_rev_str.insert(0,s)
        	else: x_rev_str.append(s)
        res = int(functools.reduce(lambda x,y: x + y, x_rev_str))
        if res < -2147483648 or res > 2147483648: return 0
        else: return res