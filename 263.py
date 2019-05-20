import math
class Solution:
    def isUgly(self,num: int) -> bool:
        if num < 1: return False
        factors = []
        while num % 2 == 0: 
            factors.append(2) 
            num = int(num / 2)
        for i in range(3,int(math.sqrt(num))+1,2): 
            while num % i== 0: 
                factors.append(i) 
                num = num / i 
        if num > 2: 
            factors.append(num)
        return set(factors).issubset(set([2,3,5]))