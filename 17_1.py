import itertools
import functools

class Solution:
     def letterCombinations(self,digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "": return []
        tmp = [[] for _ in range(len(digits))]
        res = []
        #print(tmp)
        for i,d in enumerate(digits):
            print(d)
            if d == "1":
                pass
            elif d == "2":
                tmp[i].append("a")
                tmp[i].append("b")
                tmp[i].append("c")
            elif d == "3":
                tmp[i].append("d")
                tmp[i].append("e")
                tmp[i].append("f")
            elif d == "4":
                tmp[i].append("g")
                tmp[i].append("h")
                tmp[i].append("i")
            elif d == "5":
                tmp[i].append("j")
                tmp[i].append("k")
                tmp[i].append("l")
            elif d == "6":
                tmp[i].append("m")
                tmp[i].append("n")
                tmp[i].append("o")
            elif d == "7":
                tmp[i].append("p")
                tmp[i].append("q")
                tmp[i].append("r")
                tmp[i].append("s")
            elif d == "8":
                tmp[i].append("t")
                tmp[i].append("u")
                tmp[i].append("v")
            elif d == "9":
                tmp[i].append("w")
                tmp[i].append("x")
                tmp[i].append("y")
                tmp[i].append("z")
            else:
                tmp[i].append(" ")
        for l in list(itertools.product(*tmp)):
                res.append(functools.reduce(lambda x,y: x+y, l))
        return res