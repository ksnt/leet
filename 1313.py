import itertools

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        i = 0
        result = []
        while i < nums_length:
            result.append(nums[i] * [nums[i+1]])
            i = i + 2
        return list(itertools.chain.from_iterable(result))