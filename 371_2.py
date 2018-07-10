# inefficient version
def getSum(a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        #res = []
        if a < 0:
            res = [-1 for i in range(-a)]
        if a >= 0:
            res = [1 for i in range(a)]
        if b < 0:
            res.extend([-1 for i in range(-b)])
        if b >= 0:
            res.extend([-1 for i in range(b)])
        #print(res)
        return sum(res)