class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(A[0])):
            res_tmp = []
            for j in range(len(A)):
                res_tmp.append(A[j][i])
            res.append(res_tmp)
        return res