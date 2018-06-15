class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        import numpy as np
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        return np.median(nums1+nums2).item()