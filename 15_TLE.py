import itertools

def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ns = [sorted(l) for l in list(itertools.combinations(nums,3)) if sum(l) == 0]
        return get_unique_list(ns)