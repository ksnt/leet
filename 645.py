class Solution:
    def findErrorNums(self,nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup = sum(nums) - sum(set(nums))
        miss = (set(x for x in range(1,len(nums)+1)) - set(nums)).pop()
        return [dup,miss]