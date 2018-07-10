# inefficient way
class Solution:
    def singleNumber(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = { x : nums.count(x) for x in nums }
        return [k for k, v in freq.items() if v == 1][0]