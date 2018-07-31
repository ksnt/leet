class Solution:
    def findTheDifference(self,s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #result = sorted(t).copy()
        t = sorted(t)
        for v in sorted(s):
            if v in t:
                t.remove(v)
        return t[0]