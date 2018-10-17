class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        left =[]
        #right = []
        count = 0
        if S is "": return 0
        for s in S:
            if s == "(":
                left.append(1)
            else:
                if left:
                    left.remove(1)
                else:
                    count = count + 1
        res = count + len(left)
        return res