import functools
class Solution:
    def convert(self,s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows or numRows==1:
            return s
        res = [[] for _ in range(numRows)]
        mod_base = 2*numRows - 2
        for i in range(len(s)):
            j = i % mod_base
            if j <= numRows -1:
                res[j].append(s[i])
            else:
                res[mod_base - j].append(s[i])
        return functools.reduce(lambda x,y: x+y, functools.reduce(lambda x,y: x+y,res))