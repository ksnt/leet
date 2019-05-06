import copy
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        dp = copy.copy(nums)
        for i in range(1,length):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)