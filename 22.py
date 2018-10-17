import functools
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        count = 0
        res = []
        res_str = []
        # orders
        # 1 -> "("
        # 0 -> ")"
        orders = [ l for l in list(itertools.product([1,0],repeat=2*n)) if sum(l)==n and l[0]==1 and l[-1]==0]
        for o in orders:
            for e in o:
                if count < 0:
                    break
                if e == 1:
                    count = count + 1
                elif e==0:
                    count = count - 1
            if count >= 0:
                res.append(o)
            count = 0 # reset
        #print(res)
        for i in range(len(res)):
            res_str.append(functools.reduce(lambda x,y: x+y,list(map(lambda x: "(" if (x == 1)  else ")",res[i]))))
        return res_str