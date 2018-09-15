class Solution:
    def getRow(self,rowIndex):
        """
        :type rowIndex: int
        :rtype: List[List[int]]
        """
        for row_num in range(rowIndex+1):
            r = [None for _ in range(row_num+1)]
            r[0] = 1
            r[-1] = 1
            for i in range(1, len(r)-1):
                r[i] = result[i-1] + result[i]
            result = r
            #print(result)
        return result