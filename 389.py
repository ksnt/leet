class Solution:
    def findTheDifference(self,s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = sorted(t).copy()
        for v in sorted(s):
            if v in result:
                result.remove(v)
        return result[0]