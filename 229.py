import collections
class Solution(object):
    def majorityElement(self,nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        list_length = len(nums)
        c = collections.Counter(nums)
        for t in c.items():
            if t[1] > (list_length / 3):
                res.append(t[0])
        return res
