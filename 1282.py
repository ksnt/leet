import collections
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        g = collections.defaultdict(list)
        for m,n in enumerate(groupSizes):
            g[n].append(m)
        result = []
        for k, v in g.items():
            l = 0
            while l < len(v):
                result.append(v[l:l+k])
                l = l + k
        return result