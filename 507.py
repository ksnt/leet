class Solution:
    def checkPerfectNumber(self,num):
        """
        :type num: int
        :rtype: bool
        """
        import math
        if num <= 0: return False
        s = 0
        for i in range(1,math.ceil(math.sqrt(num))):
            if num % i == 0:
                s = s + i
                if i * i != num:
                    s = s + num // i
        return s - num == num
