class Solution:
    def lengthOfLastWord(self,s):
        """
        :type s: str
        :rtype: int
        """
        if s == "": return 0
        s = s.rstrip()
        length = 0
        for i in range(len(s),0,-1):
            if s[i-1] != " ":
                length = length + 1
            else:
                break
        return length