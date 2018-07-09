from functools import reduce
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        for s in str(int(reduce(lambda x,y: x + y,map(str,digits))) + 1):
            res.append(s)
        return list(map(int,res))