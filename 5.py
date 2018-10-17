class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        length = len(s)


        if length == 0:
            return ""
        if length == 1:
            return s
        if s == s[::-1]:
            return s

        for i,e in enumerate(s):
            add = 1
            while i + add <= length:
                tmp = s[i:i+add]
                if tmp == tmp[::-1]:
                    res.append(tmp)
                add = add + 1
        return max(res, key=len)