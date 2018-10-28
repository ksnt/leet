import math
class Solution:
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        N = int(N)
        if N == 1: return 2
        while not (self.isPalindrome(N) and self.isPrime(N)):
            if N % 2 == 0:
                N = N + 1
            else:
                N = N + 2
        return N
    
    def isPrime(self,n):
        if n < 2:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        else:
            sqrt = math.ceil(math.sqrt(n))
            for i in range(2,sqrt+1):
                if n % i == 0: return False
            return True
    
    def isPalindrome(self,n):
        if n < 10 == 1: return True
        n_str = str(n)
        n_list = list(n_str)
        if n_list == n_list[::-1]:
            return True
        else:
            return False