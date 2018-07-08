class Solution:
    def toGoatLatin(self,S):
        """
        :type S: str
        :rtype: str
        """
        l = S.split(" ")
        res = []
        for s in list(enumerate(l)):
            if s[1][0] in ["a","e","i","o","u","A","E","I","O","U"]:
                res.append(s[1]+"ma"+"a"* (s[0]+1))
            else:
                res.append(s[1][1:]+s[1][0]+"ma"+"a"* (s[0]+1))
        return(" ".join(res))