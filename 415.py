import functools
class Solution:
    def addStrings(self,num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        if len(num1) < len(num2):
            tmp = num2
            num2 = num1
            num1 = tmp
        num2 = num2.zfill(len(num1))
        carry = 0
        for i in range(len(num1)-1,-1,-1):
            num = int(num1[i]) + int(num2[i]) + carry
            if num >= 10:
                n = num%10
                carry = 1
                res.insert(0,n)
            else:
                n = num%10
                carry = 0
                res.insert(0,n)
        if carry == 1: res.insert(0,carry)
        return functools.reduce(lambda x,y: x + y,list(map(str,res)))