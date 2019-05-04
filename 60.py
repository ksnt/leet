import itertools
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1,n+1)]
        return "".join(list(map(str,list(itertools.permutations(nums))[k-1])))