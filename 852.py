class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        prev = -1
        for i in range(len(A)):
            if A[i] < prev:
                return i-1
            else:
                prev = A[i]
        return i