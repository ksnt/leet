class Solution:
    def prefixesDivBy5(self,A: List[int]) -> List[bool]:
        result = []
        value = 0
        for a in A:
            value = value * 2
            value = value + a
            if value % 5 == 0:
                result.append(True)
            else:
                result.append(False)
        return result