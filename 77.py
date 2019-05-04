import itertools
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        return [list(l) for l in list(itertools.combinations(nums,k))]