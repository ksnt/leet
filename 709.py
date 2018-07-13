class Solution(object):
    def toLowerCase(self,str):
        """
        :type str: str
        :rtype: str
        """
        res = ""
        for s in str:
            if ord(s) >= 65 and ord(s) <= 90:
                res = res + chr(ord(s) + 32)
            else:
                res = res + s
        return res