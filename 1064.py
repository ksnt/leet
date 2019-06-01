class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        min_index = -1
        for i,a in enumerate(A):
            if i == a:
                min_index = i
                return min_index
        return min_index