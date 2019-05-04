class Solution:
    def threeSumClosest(self,nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)):
            #print(res)
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s-target) < abs(res-target):
                    res = s
                if s < target:
                    l = l + 1
                elif s > target:
                    r = r - 1
                else:
                    return res
        return res