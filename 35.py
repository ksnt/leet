class Solution:
    def searchInsert(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in enumerate(nums):
            if i[1] >= target:
                return i[0]
        return len(nums)