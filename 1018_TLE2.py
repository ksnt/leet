class Solution:
    def prefixesDivBy5(self,A: List[int]) -> List[bool]:
        result = []
        for i in range(1,len(A)+1):
            result.append((int(''.join(list(map(str,A[:i]))),2)%5==0))
        return result