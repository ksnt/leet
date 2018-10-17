class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        Think a + b = -c
        Set c, then
        Search (a,b)
        """
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                """ avoid duplication"""
                continue
            target = nums[i] * -1
            j,k = i+1, n-1
            while j < k:
                if nums[j] + nums[k] == target:
                     res.append([nums[i],nums[j],nums[k]])
                     j = j + 1
                     while j < k and nums[j] == nums[j-1]:
                         j = j + 1
                elif nums[j] + nums[k] < target:
                    j = j + 1
                else:
                    k = k -1
        return res