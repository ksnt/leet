from math import sqrt 
from math import ceil 
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        return [i for i in range(0, ceil(sqrt(c))+1) if c-i*i >=0 and sqrt(c - i * i).is_integer()] != []