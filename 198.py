#Solution using DP
class Solution:
    def rob(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp_restore = [0,0]
        for i in range(2,len(nums)+2):
            dp_restore.append(max(dp_restore[i-2]+nums[i-2],dp_restore[i-1]))
        #print(dp_restore)
        return dp_restore[-1]