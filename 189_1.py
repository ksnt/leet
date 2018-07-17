# Inefficient
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        i = 0
        while(i < k):
            nums[:] = nums[-1:] + nums[:-1]
            i = i+1