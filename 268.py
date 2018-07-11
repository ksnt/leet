class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (set([i for i in range(len(nums)+1)]) - set(nums)).pop()