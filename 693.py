class Solution:
    def hasAlternatingBits(self,n):
        """
        :type n: int
        :rtype: bool
        """
        binary = bin(n)[2:]
        flag = 1
        binary_list = [b for b in binary]
        for b in binary_list[1:]:
            if int(b) == flag:
                return False
            else:
                if int(b) == 0:
                    flag = 0
                else:
                    flag = 1
        return True