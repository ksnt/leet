import collections
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        res.append(collections.Counter(nums).most_common()[-1][0])
        res.append(collections.Counter(nums).most_common()[-2][0])
        return res