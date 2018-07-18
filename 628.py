class Solution:
    def maximumProduct(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        nums_neg = [n for n in nums if n < 0]
        #nums_pos = [n for n in nums if n >= 0]
        if len(nums_neg) >= 2:
            return max(nums_neg[0] * nums_neg[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
        else:
            return nums[-1] * nums[-2] * nums[-3]