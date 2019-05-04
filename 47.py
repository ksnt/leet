import itertools

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return [list(l) for l in list(set(itertools.permutations(nums)))]