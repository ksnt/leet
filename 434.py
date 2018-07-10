import re
class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip(" ")
        s = s.lstrip(" ")
        if s == "": return 0
        s = re.sub(r"\s+", " ", s)
        sum = 1
        for ch in s:
            if ch == " ":
                sum = sum + 1
        return sum