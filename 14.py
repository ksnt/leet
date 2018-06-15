class Solution:
    def longestCommonPrefix(self,strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if strs == []: return res
        if len(strs) == 1:
            return strs[0]
        else:
            list_length = len(strs)
        strs.sort(key=len) # sort according to the lenth of each element
        for i in range(len(strs[0])):
            str_i = 1
            while str_i < list_length:
                if strs[0][i] != strs[str_i][i]: return res
                str_i += 1
            res = res + strs[0][i]
        return res