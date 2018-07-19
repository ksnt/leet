#TLE
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return [i for i,x in enumerate(A) if x == max(A)][0]