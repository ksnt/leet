class Solution:
    def generate(self,numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for row_num in range(numRows):
            r = [None for _ in range(row_num+1)]
            r[0] = 1
            r[-1] = 1
            for i in range(1, len(r)-1):
                r[i] = result[row_num-1][i-1] + result[row_num-1][i]
            result.append(r)
        return result