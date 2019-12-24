class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] in result:
                result.remove(nums[i])
            else:
                result.append(nums[i])
        return result[-1]