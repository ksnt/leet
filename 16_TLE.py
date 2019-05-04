class Solution:
    import itertools
    import sys
    def threeSumClosest(self, nums: 'List[int]', target: 'int') -> 'int':
        min_num = sys.maxsize
        res = 0
        for i in list(map(sum,list(itertools.combinations(nums, 3)))):
            if abs(i - target) < min_num:
                min_num = abs(i - target)
                res = i
        return res