import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(i) for i in list(itertools.permutations(nums))]