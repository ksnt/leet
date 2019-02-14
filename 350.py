class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        res = []
        for n1 in nums1:
            for j,n2 in enumerate(nums2):
                if n1 == n2:
                    res.append(n1)
                    del nums2[j]
                    break
        return res