class Solution:
    def diStringMatch(self,S):
        """
        :type S: str
        :rtype: List[int]
        """
        l = 0
        r = len(S)
        index = [i for i in range(len(S)+1)]
        result = []
        for s in S:
            if s == "I":
                #print(l)
                result.append(index[l])
                l = l + 1
            if s == "D":
                #print(r)
                result.append(index[r])
                r = r -1
        result.append(index[l])
        return result