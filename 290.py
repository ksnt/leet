class Solution:
    def wordPattern(self,pattern:str, str: str) -> bool:
        dic = {}
        if len(pattern) == len(str):
            return False
        else:
            l = str.split()
        if len(pattern) != len(l):
            return False
        for i in range(len(pattern)):
            print(dic)
            if pattern[i] not in dic.keys():
                if l[i] in dic.values():
                    return False
                else:
                    dic[pattern[i]] = l[i]
            else:
                if dic[pattern[i]] == l[i]:
                    pass
                else:
                    return False
        return True