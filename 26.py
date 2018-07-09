class Solution:
    def removeDuplicates(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        seen_add = seen.add
        nums[:] =  [ x for x in nums if x not in seen and not seen_add(x)]
        return len(nums)