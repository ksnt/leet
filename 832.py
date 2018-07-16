class Solution:
    def flipAndInvertImage(self,A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for a in A:
            tmp = []
            for a_i in a[::-1]:
                if a_i == 0:
                    tmp.append(1)
                else:
                    tmp.append(0)
            res.append(tmp)
        return res