class Solution:
    def checkPerfectNumber(self,num):
        """
        :type num: int
        :rtype: bool
        """
        divisors = [1]
        for i in range(2,num//2 + 1): # the same as math.floor
            if num % i == 0: divisors.append(i)
        #print(divisors)
        if sum(divisors) == num:
            return True
        else:
            return False