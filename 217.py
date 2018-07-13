class Solution(object):
    def containsDuplicate(self,nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return True if len(list(set(nums))) != len(nums) else False