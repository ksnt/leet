import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [c[0] for c in collections.Counter(nums).most_common()[:k]]