class Solution:
    def isIsomorphic(self,s: str, t: str) -> bool:
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic.keys():
                if t[i] in dic.values():
                    return False
                else:
                    dic[s[i]] = t[i]
                    #print(dic)
            else:
                if dic[s[i]] == t[i]:
                    pass
                else:
                    return False
        return True