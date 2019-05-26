import sys
sys.setrecursionlimit(10000000)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0: return 0
        fact = self.factorial(n)
        res = 0
        while(fact >= 10):
            if fact % 10 == 0:
                res += 1
                fact = fact // 10
            else:
                break
        return res
    
    def factorial(self,n: int) -> int:
        if n == 0: return 1
        elif 
        else: return n * self.factorial(n-1)